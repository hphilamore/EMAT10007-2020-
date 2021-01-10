#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 22:03:36 2020

@author: hemma
"""
import statistics
import os
import matplotlib.pyplot as plt
import numpy as np
import math
import csv


###############################
# Part 1 Question 1 & 2
###############################

# A function which asks the user for the mode, rotation and the message
def AskUser():
    
    # Part 3 Question 1
    EntryMode = GetEntryMode()
    Message = GetMessage(EntryMode)

    # Part 1 Question 1
    Mode = GetMode()

    # Part 4 Question 2
    if (Mode == 'auto-decryption'):
        CommonWords = ReadWordsTxt()
        OutputMessage = AutoDecrypt(Message,CommonWords)
    

    # Part 1 Question 5
    if (Mode == 'encryption'):
        Rotation = GetRotation()
        print("Encrypted message:")
        # encrypt each line
        OutputMessage = [ Encrypt(Line, Rotation) for Line in Message ]
    
    if (Mode == 'decryption'):
        Rotation = GetRotation()
        print("Decrypted message:")
        # decrypt each line
        OutputMessage = [ Decrypt(Line, Rotation) for Line in Message ]

    print(OutputMessage)
    print()

    # Part 2 Question 2
    Top10 = GetCommonWords(OutputMessage)
    for (Count,Word) in Top10:
        print(Word,':',Count)



# A function which asks the user for the mode (encryption or decryption)
def GetMode():
    # X will store the user's input
    X = ''
    # Mode will store either 'encryption' or 'decryption'
    Mode = ''

    # loop through asking the user for an input until they press 'e' or 'd'
    # note that we want an & here not an | (or)
    while (X != 'e') & (X != 'd'):
        
        print("Please press either 'e' for encryption and 'd' for decryption, then press enter.")
        X = input()
        
        # check for the right input
        if (X == 'e'):
            Mode = 'encryption'
        elif (X == 'd'):
            Mode = 'decryption'
        else:
            print("Invalid input.")
    
    # Part 4 Question 1
    if (Mode == 'decryption'):
        # ask if they want auto-decryption
        print()
        print("Do you want auto-decryption?")
        print("Press Y for yes and N for no, then press enter.")
        X = input()
        
        # check for valid entry
        while (X != 'Y') & (X != 'N'):
            print("Invalid entry.")
            X = input()

        # if the user wants auto-decryption, set the mode
        if (X == 'Y'):
            Mode = 'auto-decryption'

    print()
    return Mode



# A function which asks the user for the rotation value
def GetRotation():
    # Rotation will store the user's input
    Rotation = -1

    # loop through asking the user for an input until they give a value between 0 and 26
    while (Rotation < 0) | (Rotation > 26):
        
        print("Please enter a number between 0 and 26, then press enter.")
        Rotation = input()

        # we want to convert from string to int, however this does not work if the string is empty
        # if the string is empty, then set Rotation to arbitrary value
        if (Rotation == ''):
            Rotation = -1
        else:
            Rotation = int(Rotation)
        
        # check for the right input
        if (Rotation >= 0) & (Rotation <= 26):
            return Rotation
        else:
            print("Invalid input.")
    print()



# A function which asks the user for the message
def GetMessage(EntryMode):
    # Part 3 Question 2
    if (EntryMode == 'manual'):
        print("Please enter your message.")
        X = input()
        # store into a list
        Message = [X]
    
    elif (EntryMode == 'read'):
        print("Please enter your file name (including the extension, e.g '.txt') which you wish to read in for the message.")
        FileName = input()
        
        # Part 3 Question 4
        # check to see if the file exists
        # FileFound is a boolean value of whether python can find the file in your current directory
        FileFound = os.path.exists(FileName)

        while (FileFound == False):
            print("File cannot be found. Please try again.")
            FileName = input()
            FileFound = os.path.exists(FileName)
        
        # Part 3 Question 3
        File = open(FileName, "r")
        Lines = File.readlines() # reads the file line by line
        Message = [ x.strip() for x in Lines ] # get rid of the \n in each line using strip()
    
    else:
        print("Error occured in 'GetMessage'.")
        Message = ['']
    print()
    return Message




###############################
# Part 1 Question 3
###############################

# A function to apply a Caeser cypher to 'Message' with a set 'Rotation'
def Encrypt(Message, Rotation):
    # convert the message to lower case first
    Message = Message.lower()
    # stores the encrypted message as a list of characters (will then be converted to a list at the end)
    Encryption = []

    # for each character, add the shift
    for Letter in Message:
        # use the ord() function to turn the character into an ASCII number
        X = ord(Letter)

        # only change the Letter if it's actually a letter (not punctuation)
        # in ASCII, a = 97 and z = 122
        if (X >= 97) & (X <= 122):
            # apply the shift
            X = X + Rotation
            # apply a wrap-around (if we shift above z then start back at a and other way round)
            if (X > 122) | (X < 97):
                X = 96 + ((X - 122) % 26)
        
        # use chr() to convert the ASCII number back into a character
        Letter = chr(X)
        # store the letter
        Encryption.append(Letter)

    # convert the output message from a list to a string using join()
    # the separator defines the character to be placed between each element of the list (in this case none)
    Separator = ''
    Output = Separator.join(Encryption)
    return Output



# A function to decrypt a Caeser cipher applied to 'Message' with a set 'Rotation'
def Decrypt(Message, Rotation):
    # we can apply decryption using the same method as encryption, but changing the Rotation
    Decryption = Encrypt(Message, -Rotation)
    return Decryption




###############################
# Part 2 Question 1
###############################

# Returns the same message, but without the punctuation
def RemovePunctuation(Message):
    Message = Message.lower()
    # will store the same message, but without the punctuation
    OutputString = ''
    
    # go through each letter and check it
    for Letter in Message:
        # get the ASCII character number
        X = ord(Letter)
        # only add this letter to the output string if it is a letter or a space (ASCII value 32)
        IsLetter = (X >= 97) & (X <= 122)
        IsSpace = (X == 32)

        if (IsLetter) | (IsSpace):
            OutputString += Letter
    return OutputString



def CountWords(Message):
    # remove the punctuation (apostrophes may count a word (such as don't) as 2 separate words)
    Message = RemovePunctuation(Message)

    # if we have an empty message, return 0
    if (Message == ''):
        WordCount = 0
    else:
        # split the message by the spaces
        Words = Message.split(' ')
        # count the words
        WordCount = len(Words)
        
        
        
    return WordCount



def CountUniqueWords(Message):
    # remove the punctuation to get just the words ("hello," is different to "hello")
    Message = RemovePunctuation(Message)
    # split the message by the spaces into words
    Words = Message.split(' ')
    # convert the list into a set
    Words = set(Words)
    # count the elements
    Count = len(Words)
    return Count, Words



def GetCommonWords(Message):
    # Message is a list of the lines
    # convert into a paragraph for this exercise
    Message = '. '.join(Message)
    # first get the unique words and the count
    Count, UniqueWords = CountUniqueWords(Message)
    # convert the message to a list of words
    Message = Message.lower()
    Words = Message.split(' ')
    # Store the words and the counts as a list of tuples (useful for when sorting)
    WordCounts = []
    
    lengths = [len(w) for w in UniqueWords]
    ave_len = np.mean(lengths)  
    print("MEAN", ave_len)
    

    for Word in UniqueWords:
        # count the occurences of the word in the message
        # use a list comprehension to print a 1 for each occurence of the word
        Counts = [1 for x in Words if (x == Word)]
        # count the number of times 1 is printed
        Count = len(Counts)
        # add the word and count to the list (we want the count first for sorting later)
        Tuple = (Count, Word)
        WordCounts.append(Tuple)

    # sort the list by the word count - sorted() will sort the tuples by the first elements
    SortedWords = sorted(WordCounts)
    # reverse the list to have descending order
    SortedWords.reverse()
    
    # get the first 10 words
    Stop = min(10, len(SortedWords)) # use min(10,n) incase n < 10 where n is the number of words
    Top10 = SortedWords[0:Stop]
    return Top10



def WordStats(Message):
    # punctuation will affect the word lengths
    Message = RemovePunctuation(Message)
    # split into words
    Words = Message.split(' ')
    # get the lengths of each word
    Lengths = [ len(x) for x in Words ]
    Minimum = min(Lengths)
    Maximum = max(Lengths)
    Mean = statistics.mean(Lengths)
    return Minimum, Maximum, Mean


def MostCommonLetter(Message):
    Message = RemovePunctuation(Message)
    # will be a list of length 26 storing the counts for each letter and the letter
    LetterCounts = []

    # for each letter in the alphabet, count the occurences (working in ASCII)
    for X in range(97, 123): # don't forget to include 122 (z) in the range
        # X to letter
        Letter = chr(X)
        Counts = [ 1 for x in Message if (x == Letter) ]
        Count = len(Counts)
        Tuple = (Count, Letter)
        LetterCounts.append(Tuple)

    # sort the list by the count (standard when the count is the first element in the tuples)
    SortedLetters = sorted(LetterCounts)
    # reverse the list to descending order
    SortedLetters.reverse()
    MostCommonTuple = SortedLetters[0]
    MostCommonLetter = MostCommonTuple[1]
    return MostCommonLetter



###############################
# Part 3 Question 1
###############################


def GetEntryMode():
    print("How would you like to input your message?")
    print("Press A for 'manual entry'.")
    print("Press B for 'read from file'.")
    print("Press enter once chosen.")
    X = input()
    
    while (X != 'A') & (X != 'B'):
        print("Invalid entry.")
        X = input()

    # convert from A and B to 'manual' and 'read'
    if (X == 'A'):
        X = 'manual'
    elif (X == 'B'):
        X = 'read'
    
    print()
    return X



###############################
# Part 4 Question 2
###############################


def ReadWordsTxt():
    # read in the words.txt file
    File = open("words.txt", "r")
    Lines = File.readlines() # reads the file line by line
    Words = [ x.strip() for x in Lines ] # get rid of the \n in each line using strip()
    return Words



###############################
# Part 4 Question 3
###############################

def AutoDecrypt(Message, CommonWords):
    # get just the first line of the message
    FirstLine = Message[0]

    # for each possible decryption rotation
    for Rotation in range(26):
        # decrypt the message
        Decryption = Decrypt(FirstLine,Rotation)

        # check to see if any of the words match
        Decryption2 = RemovePunctuation(Decryption)
        Words = Decryption2.split(' ')
        for Word in Words:
            if (Word in CommonWords):
                print("Is the following line fully decrypted?")
                print("Press Y for yes and N for no, then press enter:")
                print(Decryption)
                X = input()
                
                # check that the input is either Y or N
                while (X != 'Y') & (X != 'N'):
                    print("Invalid entry")
                    X = input()

                # if the first line is fully decrypted, then decrypt whole file and return that
                if (X == 'Y'):
                    FullDecryption = [ Decrypt(Line,Rotation) for Line in Message ]
                    print("Rotation: ", Rotation)
                    return FullDecryption



# ###############################
# # Part 5 Question 1
# ###############################

# # Can call AskUser() and do it manually
# # This decrypts the file automatically (using hard coded parameters - I got these from observing AskUser())
# # I made this function so testing the later functions was a faster process
# def GetData():
#     # Read in the data
#     FileName = 'douglas_data_encrypted.txt'
#     File = open(FileName, "r")
#     Lines = File.readlines() # reads the file line by line
#     Message = [ x.strip() for x in Lines ] # get rid of the \n in each line using strip()
#     Decryption = [ Decrypt(Line, 6) for Line in Message ]
#     return Decryption


# def FormatData(Message):
#     KnotRatios = []
#     Es = []
#     BeamHeights = []
#     BendingStrengths = []
#     for Line in Message:
#         # we only need the lines which start with 'do' (actually contains data)
#         if (Line.find('do') == 0):
#             # split the line into the separate data values
#             Data = Line.split(' ')
#             KnotRatios.append(float(Data[2]))
#             Es.append(float(Data[4]))
#             BeamHeights.append(float(Data[6]))
#             BendingStrengths.append(float(Data[7]))
#     Features = [KnotRatios, Es, BeamHeights, BendingStrengths]
#     return Features




# ###############################
# # Part 5 Question 2
# ###############################

# def PlotData():
#     Data = GetData()
#     Features = FormatData(Data)
#     X = np.array(Features[3]) # bending strengths
#     Y = np.array(Features[0]) # knot ratios

#     # get the fitted line
#     U = np.polyfit(X, Y, 1)
#     V = np.poly1d(U)

#     plt.style.use('ggplot')
#     # plot the data point
#     plt.scatter(X,Y, color='grey')
#     # plot the fitted line
#     plt.plot(X, V(X))
#     # formatting the plot
#     plt.xlabel("Bending Strength (n/mm2)")
#     plt.ylabel("Knot Ratio")

#     # Part 5 Question 4
#     plt.savefig("plot.pdf")
#     plt.show()

#     # Part 5 Question 3
#     # calculate the epislon values using a list comprehension and zipping the raw and fitted values together
#     YValues = zip(Y, V(X))
#     Epsilon = [ raw - fitted for (raw, fitted) in YValues ]
#     # change to numpy array so we can square it
#     Epsilon = np.array(Epsilon)
#     Epsilon2 = Epsilon * Epsilon
#     N = len(Epsilon2)
#     RMSE = math.sqrt( (1/N) * sum(Epsilon2) )
#     print(RMSE)




# ###############################
# # Part 5 Question 1
# ###############################

# def GetBendingStiffness():
#     Data = GetData()
#     Features = FormatData(Data)
#     # E is stored in (kg/m3) unit and BeamHeights stored in (cm)
#     Es = Features[1] # can find the ordering of the features at the end of FormatData()
#     BeamHeights = Features[2]
#     # convert to a numpy array
#     E = np.array(Es)
#     BeamHeights = np.array(BeamHeights)
#     # correct the units
#     BeamHeights = BeamHeights * 10

#     b = 1
#     I = (b**4) / 12.0
#     L = BeamHeights - 10
#     L = np.array(L)
#     L3 = L*L*L
#     # get the reciprocal as you cannot divide lists/array, but you can multiply (element-wise)
#     L3Reciprocal = [ (1/x) for x in L3 ]
#     BendingStiffness = (3 * E * I) * L3Reciprocal
    
#     # edit the data to add the bending stiffness into it and format to put into a cvs
#     Rows = []
#     n = len(Data)
#     # for each data point
#     for i in range(2,n): # we don't want to count the first 2 lines
#         LineString = Data[i]
#         # Convert the string into a list
#         LineList = LineString.split(' ')
#         LineList.append(BendingStiffness[i-2])
#         Rows.append(LineList[1::])

    
#     # writing to csv file  
#     with open('data.csv', 'w') as csvfile:  
#         # creating a csv writer object  
#         csvwriter = csv.writer(csvfile)  
        
#         # writing the data rows  
#         csvwriter.writerows(Rows)

AskUser()
# PlotData()
# GetBendingStiffness()