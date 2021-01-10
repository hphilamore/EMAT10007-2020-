#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:18:30 2020

@author: hemma
"""
import numpy as np
from os.path import exists
import metrics
import matplotlib.pyplot as plt
import random

# PART 1.3
def encrypt(shift, msg):
    """ 
    Encrypt the mes-sage by the provided shift by passing 
    the message and rotation value to anencryptionfunction 
    as arguments.  
    The program should then print the encrypted message
    https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
    """ 
    encrypted = ""
    msg = msg.upper()       # PART 1.5 All messages returned as UPPER CASE only.
    collect_metrics(msg)    # PART 2.1 collect data on unencryted text
    for ch in msg:
        if ch.isalpha():               # PART 1.5 Only characters encrypted, numbers, punctuation and spaces unchanged
            #ch = ch.upper()           # PART 1.5 All messages returned as UPPER CASE only.
            new_ch = ord(ch) + shift   # shift 
            if new_ch > ord('Z'):      # correct if over-shot
                new_ch -= 26
            elif new_ch < ord('A'):    # correct if over-shot
                new_ch += 26
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
    msg = msg.upper()       # PART 1.5 All messages returned as UPPER CASE only.
    for ch in msg:
        if ch.isalpha():               # PART 1.5 Only characters decrypted, numbers, punctuation and spaces unchanged
            #ch = ch.upper()           # PART 1.5 All messages returned as UPPER CASE only.
            new_ch = ord(ch) - shift   # shift 
            if new_ch > ord('Z'):      # correct if over-shot
                new_ch -= 26
            elif new_ch < ord('A'):    # correct if over-shot
                new_ch += 26
            ch = chr(new_ch)
        decrypted+=ch
    collect_metrics(decrypted)         # PART 2.1 collect data on unencryted text 
    #print(decrypted + "\n")
    return(decrypted)

def auto_decrypt(msg):
    """ 
    Decrypts input message by shifting number of places,
    checking for matches using common words file and promoting
    the user to verify, and shifting again if necessary
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
        
        # PART 4.3.b.i attempt to match words with words found in the common words list.
        #decrypted = decrypt(i, msg).split()
        decrypted = decrypt(i, msg).split('\n', 1)[0] # select first line of file         
        #decrypted = decrypted.split()  # split line into list of words
        intersection = set(decrypted.split()) & set(common_caps)

        # PART 4.3.b.ii If matches discovered, present line to user to check
        if len(intersection)!=0:
            check = input("English word match found: \n" +
                          decrypted + 
                          "\n \n Match found? y/n \n")           
            # PART 4.2.b.iii 
            # If user verifies decrytion, decrypt rest of file using this rotation
            if check == 'y':
                print(decrypt(i, msg) + "\n")
                collect_metrics(decrypt(i, msg)) # PART 2.1 collect data on unencryted text
                return decrypt(i, msg)
    

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

# Returns the same message, but without the punctuation
def remove_punctuation(msg):
    # will store the same message, but without the punctuation
    out = ''
    
    # go through each letter and check it
    for ch in msg:
        # get the ASCII character number
        x = ord(ch)
        # only add this letter to the output string if it is a letter or a space (ASCII value 32)
        IsLetter = (x >= 65) & (x <= 90)
        IsSpace = (x == 32)

        if (IsLetter) | (IsSpace):
            out += ch
    return out



def collect_metrics(text):
    """
    Total number of words
    Number of unique words
    Print (up to) the ten most common words sorted by their frequency
    Minimum, maximum, and average word length;
    Most common letter
    """
    #global num_words, num_unique, most_common_w ,longest, shortest, ave_len, most_common_l 
    
    #text = remove_punctuation(text)
    #print('text', text)
    text_ = remove_punctuation(text)
    #print('text_', text_.split())
    words = text_.split()
    #print(words)
    num_words = len(words)                                          # PART 2.1a : total number of words
    unique, count_W = np.unique(words, return_counts=True)          
    num_unique = len(unique)                                        # PART 2.1b : number unique words  
    most_common_w = sorted(zip(count_W, unique), reverse=True)[:10] # PART 2.1c : most common words, sorted
    # for m in most_common_w:
    #     print(f"{m[1]} : {m[0]}")
    #print('unique', unique)
    
    lengths = [len(w) for w in unique]
    
    # Z = [len(w)*c for w,c in zip(unique, count_W)]
    # print('MEAN=', np.sum(np.array(Z))/num_words)
    
    
    longest = max(lengths)                # PART 2.1d : Min word length
    shortest = min(lengths)               # PART 2.1d : Max word length
    #ave_len = np.mean(np.array(lengths))            # PART 2.1d : Ave word length
    
    
    #print('letters:', list(text))
    
    letters = [l for l in list(text) if 65<ord(l)<90 ] # strip out all punctuation and spaces
    
    #print('letters:', m)
    
    letters, count_L = np.unique(letters, return_counts=True)
    
    freq = max(count_L)
    most_common_l = [l for l,c in zip(letters, count_L) if c==freq] # PART 2.1e : most common letter

    metrics.num_words = num_words
    metrics.num_unique = num_unique
    metrics.most_common_w = most_common_w
    metrics.longest = longest
    metrics.shortest = shortest
    #metrics.ave_len = ave_len
    metrics.most_common_l = most_common_l
    
    
def setup():
    # PART 1.1
    # Ask for: cipher mode, rotation value, message 
    mode = None
    rot = None 
    msg = None
    input_mode = None
    rot_mode = None
    
    while not(mode == "e" or mode == "d" or mode =="a"):                # Part 4.1 Auto-decrytion mode added
        mode = input("Select encryption mode (press e + enter)," +      # PART 1.2 # Prompt user if input is invalid 
                      " or decryption mode (press d + enter)," +
                      " or auto-decryption mode (press a + enter)" +
                      "\n")
    if mode == 'e':
        print("Encryption Mode") 
    elif mode == 'a':
        print("Auto-Decryption Mode") 
    else:
        print("Decryption Mode")
    
    
    if mode !="a":
        while(rot_mode!="r" and rot_mode!="i"):
            rot_mode = input("Press i + enter to input number of places for " +
                             "cipher to shift, \n or press r + enter to shift " +
                             "by a random rotation")
            
        # PART 1.6 Alow the user to select to either enter the rotation value explicity 
        # or request tht the computer generate a random rotation value
        if rot_mode == "r":
            rot = random.randint(-26, 26)
        
        else:   
            while(not isinstance(rot, int)):
                rot = int(input("Input number of places for cipher to shift \n"))
                # while(rot <= 0):
                #     rot = int(input("Number of places for cipher to shift must be \
                #                     greater than zero, choose again \n"))
                        
        print(f"Shift cipher {rot} places")
    
    
    # PART 3.1 : Choose to input message / read in message from file
    while(input_mode!="m" and input_mode!="f"):
        input_mode = input("Press m + enter to type in a message" + 
                            " or press f + enter to read in the contents" + 
                            " of a file \n")
    # PART 3.2 : If read from file, provide filename
    if input_mode == "f":
        file_path = input("Input filename including full file path" + 
                          " and press enter. \n")
        
        # PART 3.4 : If the filename  cannot be found, print error and ask again
        # PART 3.4 : The program should then continue to work as before
        while(not exists(file_path)):
            file_path = input("Error: File does not exist. Retry entering" + 
                              " full file path and press enter. \n")
        # PART 3.3 : attempt to open a file with the name given and read in the contents
        with open(file_path, "r") as f:
            msg = f.read()
            print(msg)
           
    # PART 3.2 : If inputting message directly, type message  
    else:
        while(msg==None or msg==""):
            msg = input("Input message to decrypt/encrpt and then" + 
                        " press enter \n")
         
    #print(msg + "\n")
    return mode, rot, msg, input_mode



def print_metrics(output_msg):
    # If the output message is a string (a solution has been found) print the metrics 
    if isinstance(output_msg, str):
        print("output msg: \n", output_msg + "\n") 
        # PART 2.2 : After en/decryption print metrics : statistics should be based on the whole message
        print(f"Number of words: {metrics.num_words} \n")
        print(f"Number of unique words: {metrics.num_unique} \n")
        print(f"Minimum word length: {metrics.shortest} \n")
        print(f"Maximum word length: {metrics.longest} \n")
        #print(f"Average word length: {metrics.ave_len} \n")        
        print("Most common words")#, most_common_w) 
        for m in metrics.most_common_w:
                print(f"{m[1]} : {m[0]}")
        print("Most common letter", metrics.most_common_l)  
    else:
        print("Decrypted message not found") 


# PART 5.
def plot_metrics(output_msg):
    # If the output message is a string (a solution has been found) print the metrics 
    if isinstance(output_msg, str):
        #print(metrics.most_common_w)
        #counts, words = zip(*metrics.most_common_w)
        counts = []
        words = []
        for i in metrics.most_common_w:
            counts.append(i[0])
            words.append(i[1])
        #print(counts, list2)
        # year_groups = ['B1', 'B2', 'B3', 'M1', 'M2']
        # num_students = [500, 332, 425, 300, 200]
        
        # # 1. create an arry with posiytion of x ticks
        x_pos = np.arange((len(words)))
        
        
        # # 2. bar chart
        plt.bar(x_pos, counts)
        
        # # 3. replace x ticks with year group name
        plt.xticks(x_pos, words, rotation=45)
        
        
        # # 4. axis labels
        plt.xlabel('words')
        plt.ylabel('frequency')
   
# PART 2.3 : Save metrics as a .txt file        
def save_metrics():
    with open("metrics.txt", "w") as file:    
        file.write(f"Number of words: {metrics.num_words} \n")
        file.write(f"Number of unique words: {metrics.num_unique} \n")
        file.write(f"Minimum word length: {metrics.shortest} \n")
        file.write(f"Maximum word length: {metrics.longest} \n")
        #file.write(f"Average word length: {metrics.ave_len} \n")

        
    # file.write("Minimum, metrics.longest,maximum, and average word length: ",  
    #            metrics.shortest, metrics.ave_len,  "\n")
    
    print()
    
    
    
    
    