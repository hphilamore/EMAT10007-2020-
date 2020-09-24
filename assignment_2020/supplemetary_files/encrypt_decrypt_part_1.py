import getopt
import sys

Alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
Letters = Alphabet.split()

def Encrypt(Messages, Rotation):
    """
    Encrypts the Message by rotating the alphabet by the provided Rotation.
    :param Messages: Lines read in from file/input()
    :param Rotation: Amount of letters to rotate the alphabet by
    :return: List of encrypted messages
    """
    # Create a list to store the encrypted messages
    EncryptedMessages = []

    # Encrypt each message in Messages
    for Message in Messages:
        Message = Message.upper()
        EncryptedMessage = []
        for Letter in Message:
            if Letter in Letters:
                EncryptedMessage.append(Letters[(Letters.index(Letter) + Rotation) % len(Letters)])
            else:
                EncryptedMessage.append(Letter)

        EncryptedMessages.append("".join(EncryptedMessage))
    # Return the list of encrypted messages
    return EncryptedMessages


def Decrypt(Messages, Rotation):
    """
    Decrypts the Message by rotating in reverse the alphabet by the provided Rotation.
    :param Messages: Lines read in from file/input()
    :param Rotation: Amount of letters to rotate the alphabet by
    :return: List of decrypted messages
    """
    # Create a list to store the decrypted messages
    DecryptedMessages = []
    # Decrypt each message in Messages
    for Message in Messages:
        Message = Message.upper()
        DecryptedMessage = []
        for Letter in Message:
            if Letter in Letters:
                DecryptedMessage.append(Letters[(Letters.index(Letter) - Rotation) % len(Letters)])
            else:
                DecryptedMessage.append(Letter)

        DecryptedMessages.append("".join(DecryptedMessage))
    # Return the list of decrypted messages
    return DecryptedMessages


def ReadFile(FileName):
    try:
        with open(FileName) as File:
            Messages = File.read().splitlines()
            return Messages
    except FileNotFoundError:
        print("Sorry, cannot find any such file named %s".format(FileName))
        print("Terminating program.")
        # Cannot read file: exit the program - exit code 1 indicates an error.
        sys.exit(1)


# ---------------------------
# Main section of the program
# ---------------------------

# Gather all the arguments (minus the program name) into a list
Arguments = sys.argv[1:]

if "--encrypt" in Arguments:
    # Grab the rotation from the program's arguments
    Rotation = int(Arguments[Arguments.index("--encrypt") + 1])
    if Rotation < 0:
        print("The rotation parameter must be a positive integer.")
        sys.exit(1)

    Messages = []
    EncryptedMessages = []
    InputString = "Please enter a message to encrypt: "

    # Read in lines from either: file, or input()
    # if "--file" is passed as an argument, then read from the given file.
    if "--file" in Arguments:
        FileName = Arguments[Arguments.index("--file") + 1]
        Messages = ReadFile(FileName)
        EncryptedMessages = Encrypt(Messages, Rotation)
    else:
        PlainText = input(InputString)
        while PlainText != "":
            # Call the encryption function on each message (line)
            Messages.append(PlainText)
            PlainText = input(InputString)
        EncryptedMessages = Encrypt(Messages, Rotation)
    for Message in EncryptedMessages:
        print(Message)

    sys.exit(0)

elif "--decrypt" in Arguments:
    # Read in lines from either: file, or input()
    Rotation = int(Arguments[Arguments.index("--decrypt") + 1])
    if Rotation < 0:
        print("The rotation parameter must be a positive integer.")
        sys.exit(1)

    Messages = []
    DecryptedMessages = []
    InputString = "Please enter a message to decrypt: "

    # Read in lines from either: file, or input()
    # if "--file" is passed as an argument, then read from the given file.
    if "--file" in Arguments:
        FileName = Arguments[Arguments.index("--file") + 1]
        Messages = ReadFile(FileName)
        DecryptedMessages = Decrypt(Messages, Rotation)
    else:
        CipherText = input()
        while CipherText != "":
            # Call the encryption function on each message (line)
            Messages.append(CipherText)
            CipherText = input()
        DecryptedMessages = Decrypt(Messages, Rotation)
    for Message in DecryptedMessages:
        print(Message)

    sys.exit(0)

else:
    print("Please provide instructions for this program:")
    print("--encrypt [message, --file FileName] : encrypt message or the contents of FileName.")
    print("--decrypt [message, --file FileName] : decrypt message or the contents of FileName.")
    print("Where [...] are optional arguments.")




