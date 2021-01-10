#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:03:19 2020

@author: hemma
"""
import numpy as np
from os.path import exists
from funcs import *
import csv
import matplotlib.pyplot as plt

# PART 1.3
# def encrypt(shift, msg):
#     """ 
#     Encrypt the mes-sage by the provided shift by passing 
#     the message and rotation value to anencryptionfunction 
#     as arguments.  
#     The program should then print the encrypted message
#     https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
#     """ 
#     encrypted = ""
#     collect_metrics(msg) # PART 2.1 collect data on unencryted text
#     for ch in msg:
#         if ch.isalpha(): # PART 1.5 Only characters encrypted, numbers, punctuation and spaces unchanged
#             ch = ch.upper() # PART 1.6 All messages returned as UPPER CASE only.
#             new_ch = ord(ch) + shift   # shift 
#             if new_ch > ord('Z'):    # correct if final letter over-shot
#                 new_ch -= 26
#             ch = chr(new_ch)
#         encrypted+=ch
#     #print(encrypted + "/n")
#     return(encrypted)


# # PART 1.4
# def decrypt(shift, msg):
#     """ 
#     Decrypts input message. Same steps as encryption, except 
#     your     program should call adecryptionfunction on each 
#     message.  
#     Decryption follows the same process as encryption, only 
#     the shift goes the opposite wayby shifting input number 
#     of places. 
#     """
#     decrypted = ""
#     for ch in msg:
#         if ch.isalpha(): # PART 1.5 Only characters decrypted, numbers, punctuation and spaces unchanged
#             ch = ch.upper() # PART 1.6 All messages returned as UPPER CASE only.
#             new_ch = ord(ch) - shift   # shift 
#             if new_ch < ord('A'):    # correct if final letter over-shot
#                 new_ch += 26
#             ch = chr(new_ch)
#         decrypted+=ch
#     collect_metrics(decrypted) # PART 2.1 collect data on unencryted text 
#     #print(decrypted + "\n")
#     return(decrypted)


# Part 4.1 
# def auto_decrypt(msg):
#     """ 
#     Decrypts input message by shifting number of places,
#     checking for matches using common words file and promting
#     the user to veriffy, and shifting again if necessary
#     ASSUMES SAME ENCRYPTION FOR ALL LINES
#     """
    
#     # Part 4.2 Read in a file of common English words
#     with open("words.txt", "r") as f:
#           common = f.read().splitlines()
#           common_caps = [c.upper() for c in common]
#           #print(common_caps)
    
#     intersection = ()
    
#     # PART 4.3.a Iteratively apply the decryption function to the first line of the message
#     for i in range(25):  
#         #decrypted = decrypt(i, msg).split() 
#         # PART 4.3.b attempt to match words with words found in the common words list.
#         decrypted = decrypt(i, msg).split('\n', 1)[0] # select first line of file 
#         decrypted = decrypted.split()  # split line into list of words
#         intersection = set(decrypted) & set(common_caps)
#         #print("intersection", intersection)
#         # PART 4.3.c If matches discovered, present line to user to check
#         if len(intersection)!=0:
#             check = input("English word match found: \n" +
#                           decrypted + 
#                           "\n \n Match found? y/n \n")
             
#             # PART 4.3.c 
#             # Print the rotation for this line, and start againat with the next line,
#             # until all the lines in the message have been successfully decrypted
#             if check == 'y':
#                 print(decrypt(i, msg) + "\n")
#                 collect_metrics(decrypt(i, msg)) # PART 2.1 collect data on unencryted text
#                 return decrypt(i, msg)
    
#     print("No decryption match found")


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
                    
        
#         print("No decryption match found")
        
#     collect_metrics(output_msg) # PART 2.1 collect data on unencryted text
#     return output_msg


# PART 2.1 Collect data on text
# def collect_metrics(text):
#     """
#     Total number of words
#     Number of unique words
#     Print (up to) the ten most common words sorted by their frequency
#     Minimum, maximum, and average word length;
#     Most common letter
#     """
#     global num_words, num_unique, most_common_w ,longest, shortest, ave_len, most_common_l 
#     words = text.split()
#     num_words = len(words)
#     unique, count_W = np.unique(words, return_counts=True)
#     most_common_w = sorted(zip(count_W, unique), reverse=True)[:10]
#     # for m in most_common_w:
#     #     print(f"{m[1]} : {m[0]}")
#     num_unique = len(unique)
#     lengths = [len(w) for w in unique]
#     longest = max(lengths)
#     shortest = min(lengths)
#     ave_len = np.mean(lengths)
    
#     letters, count_L = np.unique(list(text), return_counts=True)
#     freq = max(count_L)
#     most_common_l = [l for l,c in zip(letters, count_L) if c==freq]



# PART 1.1
# Ask for: cipher mode, rotation value, message 
mode = None
rot = None 
msg = None
input_mode = None

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
    while(not isinstance(rot, int)):
        rot = int(input("Input number of places for cipher to shift \n"))
        while(rot <= 0):
            rot = int(input("Number of places for cipher to shift must be greater than zero, choose again \n"))
                
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


 
if mode=='e':
    output_msg = encrypt(rot, msg)  
elif mode == 'a':
    output_msg = auto_decrypt(msg)
else:
    output_msg = decrypt(rot, msg)


# If the output message is a string (a solution has been foudn) print the metrics 
if isinstance(output_msg, str):
    print("output msg: \n", output_msg + "\n") 
    # PART 2.2 : After en/decryption print metrics : statistics should be based on the whole message
    print("Number of words: ", metrics.num_words)
    print("Number of unique words: ", metrics.num_unique)
    print("Minimum, maximum, and average word length: ", 
          metrics.longest, metrics.shortest, metrics.ave_len,)
    
    print("Most common words")#, most_common_w) 
    for m in metrics.most_common_w:
            print(f"{m[1]} : {m[0]}")
    print("Most common letter", metrics.most_common_l)  
else:
    print("Decrypted message not found") 



#file_path = 'douglas_data_encrypted.txt'

# PART 5.1 Decrypt douglas data
if 'file_path' in globals():
    if  file_path == 'douglas_data_encrypted.txt':
        
        # ....and save decrypted data as file 
        with open("douglas_data_decrypted.txt", "w") as file:
            file.write(output_msg)
        
        
        print("Douglas")
        #print(type(output_msg))
        #with open("douglas_data.txt", "r") as file:
        with open("douglas_data_decrypted.txt", "r") as file:
            
        
            # Perform what you need to do on data
            # for row in data:
            #     print(row)
            # print(data)  
            
            data_ = list(csv.reader(file, delimiter=" "))
            data_ = [d[1:] for d in data_]
            headings = data_[0]
            #headings = [h for h in data[0] if h!= '']
            data = np.array(data_[2:]).astype(float)
            
            knot_i = headings.index('KNOT_RATIO')
            str_i = headings.index('BENDING_STRENGTH')
            E_i = headings.index('E')
            H_i = headings.index('BEAMHEIGHT')
            
            tmp = sorted(zip(data[:, knot_i], 
                             data[:, str_i]))
    
            knot = np.array([t[0] for t in tmp])
            strength = np.array([t[1] for t in tmp])
            
            # PART 5.2 Plot the data
            plt.scatter(knot, strength)
            
            coeffs = np.polyfit(knot, strength, 1)
    
            yfit = np.poly1d(coeffs)(knot)
    
            plt.plot(knot, yfit, 'r', label=f'y = {round(coeffs[0],2)}x + {round(coeffs[1],2)}')
            plt.legend()
            
            plt.xlabel('knot ratio (%)')
            plt.ylabel('bending strength (N/mm^2)')
            
            # PART 5.3 Find the RMSE
            RMSE = np.sqrt(np.sum((strength - yfit)**2)/ len(yfit))
            
            plt.title(f'RMSE = {RMSE}')
            
            #PART 5.4 Save plot as pdf
            plt.savefig('beam_plot.pdf')
            plt.show()
            
            #PART 5.5 find the bending stiffness
            E = np.array(data[:, E_i])*1_000_000
            H = np.array(data[:, H_i])/10
            
            I = 0.05**4 / 12
            
            stiffness = 3 * E * I / (H - 0.1)**2
            
            stiffness = stiffness.reshape(stiffness.shape[0],-1)
            
            print(data.shape)
            print(stiffness.shape)
            
            headings = headings + ['STIFFNES']
            data_[1] = data_[1] + ['N/MM']
            
            data = np.hstack((data, stiffness))
            
            # PART 5.6 save as .pdf file 
            with open ('beam_data.csv', 'w') as f:
                head = ",".join(headings) + "\n" + ",".join(data_[1])
                #np.savetxt('beam_data.csv', data, delimiter=',', header=",".join(headings))
                np.savetxt('beam_data.csv', data, delimiter=',', header=head)
    

        
        
        
        
        



