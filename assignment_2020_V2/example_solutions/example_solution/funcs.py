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
    """ 
    encrypted = ""
    msg = msg.upper()                  # PART 1.5 All messages returned as UPPER CASE only.
    collect_metrics(msg)               # PART 2.1 collect data on unencryted text
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
    msg = msg.upper()                  # PART 1.5 All messages returned as UPPER CASE only.
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
        decrypted = decrypt(i, msg).split('\n', 1)[0] # select first line of file         
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
    


# Returns the same message, but without the punctuation
def remove_punc(msg):
    """
    Returns message with puctuation removed 
    """
    out = ''
    
    for ch in msg:
        x = ord(ch) # convert to ASCII character
        IsLetter = (x >= 65) & (x <= 90)
        IsSpace = (x == 32)

        if (IsLetter) | (IsSpace):
            out += ch
    return out



def collect_metrics(text):
    """
    Stores metrics about the input text to external file:
    Total number of words
    Number of unique words
    Print (up to) the ten most common words sorted by their frequency
    Minimum, maximum word length;
    Most common letter
    """
    text_ = remove_punc(text)
    
    try: 
        words = text_.split()
        num_words = len(words)                                          # PART 2.1a : total number of words
        unique, count_W = np.unique(words, return_counts=True)          
        num_unique = len(unique)                                        # PART 2.1b : number unique words  
        most_common_w = sorted(zip(count_W, unique), reverse=True)[:10] # PART 2.1c : most common words, sorted 
        lengths = [len(w) for w in unique]
        longest = max(lengths)                                          # PART 2.1d : Min word length
        shortest = min(lengths)                                         # PART 2.1d : Max word length
    
        
        letters = [l for l in list(text) if 65<ord(l)<90 ]              # strip out all punctuation and spaces
        letters, count_L = np.unique(letters, return_counts=True)
        freq = max(count_L)
        most_common_l = [l for l,c in zip(letters, count_L) if c==freq] # PART 2.1e : most common letter
    
        metrics.num_words = num_words
        metrics.num_unique = num_unique
        metrics.most_common_w = most_common_w
        metrics.longest = longest
        metrics.shortest = shortest
        metrics.most_common_l = most_common_l
        
    except:
        print("Invalid message")
    
    
    
def setup():
    """
    Returns programme configuration as entered by user 
    """
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
            
        # PART 1.6 Allow the user to select to either enter the rotation value explicity 
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
         
    return mode, rot, msg, input_mode



def print_metrics(output_msg):
    """
    Prints statitics about message

    """
    # If the output message is a string (a solution has been found) print the metrics 
    if isinstance(output_msg, str):
        print("output msg: \n", output_msg + "\n") 
        # PART 2.2 : After en/decryption print metrics : statistics should be based on the whole message
        print(f"Number of words: {metrics.num_words} \n")
        print(f"Number of unique words: {metrics.num_unique} \n")
        print(f"Minimum word length: {metrics.shortest} \n")
        print(f"Maximum word length: {metrics.longest} \n")       
        print("Most common words")#, most_common_w) 
        try:
            for m in metrics.most_common_w:
                    print(f"{m[1]} : {m[0]}")
            print("Most common letter", metrics.most_common_l) 
        except:
            print("Most common letter: None")
    else:
        print("Decrypted message not found") 


# #!EXTRA# PART 5 : Produces a bar showing frequency of most common words 
def plot_metrics(output_msg):
    """
    Produces a bar showing frequency of most common words 
    """
    # If the output message is a string (a solution has been found) print the metrics 
    if isinstance(output_msg, str):
        counts = []
        words = []
        try:
            for i in metrics.most_common_w:
                counts.append(i[0])
                words.append(i[1])
        except:
            print("Empty 'most common words' list")
        
        # create an array with posiytion of x ticks
        x_pos = np.arange((len(words)))
        
        # bar chart
        plt.bar(x_pos, counts)
        
        # replace x ticks with year group name
        plt.xticks(x_pos, words, rotation=45)
        
        # axis labels
        plt.xlabel('words')
        plt.ylabel('frequency')
        
        plt.savefig("bars.pdf", bbox_inches='tight')
   
# PART 2.3 : Save metrics as a .txt file        
def save_metrics():
    """
    Saves metrics as a text file 
    """
    with open("metrics.txt", "w") as file:    
        file.write(f"Number of words: {metrics.num_words} \n")
        file.write(f"Number of unique words: {metrics.num_unique} \n")
        file.write(f"Minimum word length: {metrics.shortest} \n")
        file.write(f"Maximum word length: {metrics.longest} \n")
    #print()
    
    
    
    
    