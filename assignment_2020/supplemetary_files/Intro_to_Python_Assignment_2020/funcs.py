#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:18:30 2020

@author: hemma
"""
import numpy as np
from os.path import exists
import metrics

def encrypt(shift, msg):
    """ 
    Encrypt the mes-sage by the provided shift by passing 
    the message and rotation value to anencryptionfunction 
    as arguments.  
    The program should then print the encrypted message
    https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
    """ 
    encrypted = ""
    collect_metrics(msg) # PART 2.1 collect data on unencryted text
    for ch in msg:
        if ch.isalpha(): # PART 1.5 Only characters encrypted, numbers, punctuation and spaces unchanged
            ch = ch.upper() # PART 1.6 All messages returned as UPPER CASE only.
            new_ch = ord(ch) + shift   # shift 
            if new_ch > ord('Z'):    # correct if final letter over-shot
                new_ch -= 26
            ch = chr(new_ch)
        encrypted+=ch
    #print(encrypted + "/n")
    return(encrypted)


# PART 1.4
def decrypt(shift, msg):
    """ 
    Decrypts input message. Same steps as encryption, except 
    your     program should call adecryptionfunction on each 
    message.  
    Decryption follows the same process as encryption, only 
    the shift goes the opposite wayby shifting input number 
    of places. 
    """
    decrypted = ""
    for ch in msg:
        if ch.isalpha(): # PART 1.5 Only characters decrypted, numbers, punctuation and spaces unchanged
            ch = ch.upper() # PART 1.6 All messages returned as UPPER CASE only.
            new_ch = ord(ch) - shift   # shift 
            if new_ch < ord('A'):    # correct if final letter over-shot
                new_ch += 26
            ch = chr(new_ch)
        decrypted+=ch
    collect_metrics(decrypted) # PART 2.1 collect data on unencryted text 
    #print(decrypted + "\n")
    return(decrypted)

def auto_decrypt(msg):
    """ 
    Decrypts input message by shifting number of places,
    checking for matches using common words file and promting
    the user to veriffy, and shifting again if necessary
    ASSUMES SAME ENCRYPTION FOR ALL LINES
    """
    
    # Part 4.2 Read in a file of common English words
    with open("words.txt", "r") as f:
          common = f.read().splitlines()
          common_caps = [c.upper() for c in common]
          #print(common_caps)
    
    intersection = ()
    
    # PART 4.3.a Iteratively apply the decryption function to the first line of the message
    for i in range(25):  
        #decrypted = decrypt(i, msg).split()
        
        # PART 4.3.b attempt to match words with words found in the common words list.
        decrypted = decrypt(i, msg).split('\n', 1)[0] # select first line of file 
        
        #print(decrypted, type(decrypted), len(decrypted))
        #print(decrypted.split(), type(decrypted.split()), len(decrypted.split()))
        #decrypted = decrypted.split()  # split line into list of words
        intersection = set(decrypted.split()) & set(common_caps)
        #print("intersection", intersection)
        # PART 4.3.c If matches discovered, present line to user to check
        if len(intersection)!=0:
            check = input("English word match found: \n" +
                          decrypted + 
                          "\n \n Match found? y/n \n")           
            # PART 4.3.c 
            # Print the rotation for this line, and start againat with the next line,
            # until all the lines in the message have been successfully decrypted
            if check == 'y':
                print(decrypt(i, msg) + "\n")
                collect_metrics(decrypt(i, msg)) # PART 2.1 collect data on unencryted text
                return decrypt(i, msg)
    
    #print("No decryption match found")

# def auto_decrypt(msg):
#     """ 
#     Decrypts input message by shifting number of places,
#     checking for matches using common words file and promting
#     the user to veriffy, and shifting again if necessary
#     DECRYPTS LINE BY LINE
#     """
    
#     # Part 4.2 Read in a file of common English words
#     with open("words.txt", "r") as f:
#           common = f.read().splitlines()
#           common_caps = [c.upper() for c in common]
#           #print(common_caps)

#     output_msg = ""
    
#     print("file content", msg)
    
#     lines = msg.split('\n')
    
#     for l in lines:
#         if len(l)==0:
#             output_msg = output_msg + "\n"
#             continue          

#         # PART 4.3.a Iteratively apply the decryption function to the first line of the message
#         for i in range(25):  
#             # PART 4.3.b attempt to match words with words found in the common words list.
#             decrypted = decrypt(i, l).split()  # split line into list of words
#             intersection = set(decrypted) & set(common_caps)
#             # PART 4.3.c If matches discovered, present line to user to check
#             if len(intersection)!=0:
#                 check = input("English word match found: \n" +
#                               decrypt(i, l) + 
#                               "\n \n Match found? y/n \n")
                 
#                 # PART 4.3.c 
#                 # Print the rotation for this line, and start again with the next line,
#                 # until all the lines in the message have been successfully decrypted
#                 if check == 'y':
#                     print("rotation = ", i)
#                     output_msg = output_msg + decrypt(i, l) + "\n"   
#                     break
#         # print("No decryption match found")
    
#     lengths = [l for l in output_msg.split('\n') if len(l)!=0]
#     if len(lengths)>0:
#         print("lengths: ", lengths)
#         collect_metrics(output_msg) # PART 2.1 collect data on unencryted text
#         return output_msg
#     else:
#         return None



def collect_metrics(text):
    """
    Total number of words
    Number of unique words
    Print (up to) the ten most common words sorted by their frequency
    Minimum, maximum, and average word length;
    Most common letter
    """
    #global num_words, num_unique, most_common_w ,longest, shortest, ave_len, most_common_l 
    words = text.split()
    num_words = len(words)
    unique, count_W = np.unique(words, return_counts=True)
    most_common_w = sorted(zip(count_W, unique), reverse=True)[:10]
    # for m in most_common_w:
    #     print(f"{m[1]} : {m[0]}")
    num_unique = len(unique)
    lengths = [len(w) for w in unique]
    longest = max(lengths)
    shortest = min(lengths)
    ave_len = np.mean(lengths)
    
    letters, count_L = np.unique(list(text), return_counts=True)
    freq = max(count_L)
    most_common_l = [l for l,c in zip(letters, count_L) if c==freq]

    metrics.num_words = num_words
    metrics.num_unique = num_unique
    metrics.most_common_w = most_common_w
    metrics.longest = longest
    metrics.shortest = shortest
    metrics.ave_len = ave_len
    metrics.most_common_l = most_common_l