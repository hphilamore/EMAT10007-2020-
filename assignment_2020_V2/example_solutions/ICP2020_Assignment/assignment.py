# Encrypted Information
# Assignment for Introduction to Computer Programming, 2020
# The task requires to write some code to perform the Caesar Cipher.

# To check if a file exists
import os

# For input validation
YESNO = ["yes", "y", "no", "n"]
ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1. Encryption and Decryption
# Function Encrypt can process single string messages. 
def Encrypt(Message, Rotation):
	NewMessage = ""
	for Letter in Message:
		# Checking if the character needs to be updated 
		# (special characters are preserved)
		if Letter in ALFABET: 
			NewPosition = (ALFABET.find(Letter)+Rotation)%26
			NewMessage += ALFABET[NewPosition]
		else:
			NewMessage += Letter
	return NewMessage

# Function to process multiple lines. They should be presented 
# as a list of strings
def EncryptLines(Lines, Rotation):
	NewLines = []
	for Line in Lines:
		NewLines.append(Encrypt(Line, Rotation))
	return NewLines

# Function that asks for the action to perform and validates
# the user input too. There are essentially three modes:
# * encrypt    -- Perform Encryption
# * decrypt    -- Perform Decryption IF rotation is provided
# * automated  -- For automated decryption
def GetMode():
	Mode = ""
	while Mode not in ("encrypt", "decrypt", "e", "d"):
		Mode = input("[E]ncrypt or [d]ecrypt a message?").lower()
	if Mode not in "encrypt":
		Automated = ""
		while Automated not in YESNO:
			Automated = input("Try automated? [y/n]").lower()
		if Automated in "yes":
			Mode = "automated"
	return Mode

# Get a valid rotation value from the user
def GetRotation():
	Rotation = ""
	while not Rotation.isnumeric():
		Rotation = input("Rotation (must be integer):")
	return int(Rotation)

# Get the message from the user by allowing either manual input
# or to specify a filepath containing the lines to process
def GetMessage():
	EntryMode = ""
	while EntryMode not in ["file", "type", "f", "t"]:
		EntryMode = input("Read from [f]ile or [t]ype message?").lower()

	if EntryMode in "file":
		FilePath = ""
		while FilePath == "":
			FilePath = input("Provide the path of the (TXT) file to read")
			if not (os.path.isfile(FilePath) and FilePath.endswith(".txt")):
				print("File does not exist or is not valid")
				FilePath = ""
		Message = ReadFromFile(FilePath)
	else:
		Message = GetTypedMessage()
	return Message

# PART 3 - Messages from a file
# Reading the lines from a file and removing any special characters at the end 
# (such as new line '\n')
def ReadFromFile(FilePath):
	f = open(FilePath, "r")
	Message = []
	for Line in f.readlines():
		Message.append(Line.strip())
	f.close()
	return Message

# Allows user to type multiple lines. To exit two consecutive enters must be
# inputted
def GetTypedMessage():
	print("Type the message (hit enter twice to quit):\n")
	Message = []
	quit = 1
	while quit < 2:
		NewLine = input()
		if NewLine == "":
			quit += 1
		else:
			quit = 1
			Message.append(NewLine.upper())
	return Message

# Getting a string with no punctuation to compute the stats
# as any special characters can mess the content
def RemovePunctuation(Message):
	NewMessage = ""
	for Letter in Message:
		if Letter in ALFABET or Letter == " ":
			NewMessage += Letter
	return NewMessage

# PART 2 - Analysing messages
# Getting all the stats. Returns a dictionary with all the 
# required values
def AnalyseMessage(Message):
	Stats = {}
	NewMessage = RemovePunctuation(Message)
	Stats['TotalWords'] = len(NewMessage.split())
	Stats['NumberUniqueWords'] = len(set(NewMessage.split()))
	Stats['MinLength'] = 100
	Stats['MaxLength'] = 0
	Stats['AvgLength'] = 0
	LetterFrequency = {}
	WordFrequency = {}
	for Word in NewMessage.split():
		WordLength = len(Word)
		if WordLength < Stats['MinLength']:
			Stats['MinLength'] = WordLength
		elif WordLength > Stats['MaxLength']:
			Stats['MaxLength'] = WordLength
		Stats['AvgLength'] += WordLength
		if Word in WordFrequency:
			WordFrequency[Word] += 1
		else:
			WordFrequency[Word] = 1

		for Letter in Word:
			if Letter in LetterFrequency:
				LetterFrequency[Letter] += 1
			else:
				LetterFrequency[Letter] = 1
	Stats['AvgLength'] /= Stats['TotalWords']
	Stats['MostFrequentWord'] = GetMostFrequent(WordFrequency)
	Stats['MostFrequentLetter'] = GetMostFrequent(LetterFrequency)
	Stats['MostCommonWords'] = GetMostFrequent(WordFrequency, 10)
	return Stats

# Obtain the K most frequent element given a dictionary with element : frequency
def GetMostFrequent(Frequencies, TopK=1):
	SortedElements = sorted(Frequencies, key=Frequencies.get, reverse=True)
	MostFrequents = []
	if TopK > len(Frequencies):
		TopK = len(Frequencies)
	for k in range(TopK):
		MostFrequents.append([SortedElements[k], Frequencies[SortedElements[k]]])
	return MostFrequents

# To format the display of the stats
def PrintStats(Stats):
	for stat in Stats:
		if "most" in stat.lower():
			print("\t",stat)
			for row in Stats[stat]:
				print("\t\t", row[0], ":", row[1])
		else:
			print("\t", stat, Stats[stat])

# Reading the file of most common English words. File must be present otherwise 
# the code will crash.
def GetCommonWords():
	f = open("words.txt", 'r')
	EnglishCommonWords = []
	for Word in f.readlines():
		EnglishCommonWords.append(Word.strip().upper())
	EnglishCommonWords = set(EnglishCommonWords)
	return EnglishCommonWords

# PART 4 - Automated decryption
# Function to attempt automated descryption as per the specification
def AutomateDecryption(Message):
	EnglishCommonWords = GetCommonWords()
	Rotation = -1
	for Line in Message:
		for R in range(26):
			DecryptedMessage = Encrypt(Line, -R)
			UniqueWords = set(DecryptedMessage.split())
			Match = EnglishCommonWords & UniqueWords
			if len(Match) > 0:
				Correct = ""
				print("Found matches: ", Match)
				print(DecryptedMessage)
				while Correct not in ["yes", "y", "no", "n"]:
					Correct = input("\nIs this correct?").lower()
				if Correct in "yes":
					Rotation = R
					break
				else:
					DecryptedMessage = ""
		if R > 0:
			break
	if Rotation > 0:
		DecryptedMessage = EncryptLines(Message, -Rotation)
	return DecryptedMessage, Rotation


# Main code to execute the Caesar cipher. Note that this is done only once
if __name__ == "__main__":
	Mode = GetMode()
	Message = GetMessage()
	if Mode in "encrypt":
		Rotation = GetRotation()
		NewMessage = EncryptLines(Message, Rotation)
		EnglishText = " ".join(Message)
	elif Mode == "automated":
		NewMessage, Rotation = AutomateDecryption(Message)
		if Rotation >0:
			print("Rotation found for decryption. Rotation:", Rotation)
		else:
			NewMessage = ["FAILED!!!"]
		EnglishText = " ".join(NewMessage)
	else:
		Rotation = GetRotation()
		NewMessage = EncryptLines(Message, -Rotation)
		EnglishText = " ".join(NewMessage)
	print("Processed message:")
	print("\n".join(NewMessage))
	print("\nMessage stats:")
	Stats = AnalyseMessage(EnglishText)
	PrintStats(Stats)

