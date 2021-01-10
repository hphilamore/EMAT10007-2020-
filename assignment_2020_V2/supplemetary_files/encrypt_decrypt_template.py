import sys

# Define a global alphabet data structure so use throughout your code.
# Alphabet = ...

def Encrypt(Message, Rotation):
    # Create a list to store the encrypted letters.
    EncryptedMessage = []
    # Encrypt each letter in Message and add it to EncryptedMessage,
    # then join the letters into a string.
    # ...

    # Return the encrypted message
    return EncryptedMessage


def Decrypt(Message, Rotation):
    # Create a list to store the decrypted letters.
    DecryptedMessage = []
    # Decrypt each letter in Message and add it to DecryptedMessage,
    # then join the letters into a string.
    # ...

    # Return the decrypted message
    return DecryptedMessage


def EncryptDecrypt(Message, Rotation, Reversed = False):
    # Create a list to store the letters of the message
    Message = []
    # Apply the rotation and the rotation direction, to encrype/decrypt
    # the message as intended.
    # ...

    # Return the encrypted/decrypted message
    return Message


def ReadFile(FileName):
    try:
        # Read the contents of the file into a list,
        # where each line in the file is a new item in the list,
        # or "message" in the list of "messages".
        #...
        # Return the list of messages.
        return Messages

    except FileNotFoundError:
        print("Sorry, cannot find any such file named %s".format(FileName))
        print("Terminating program.")
        # Cannot read file: exit the program - exit code 1 indicates an error.
        sys.exit(1)


# ---------------------------
# Main section of the program
# ---------------------------

# Gather all the arguments (minus the first - the program name) in a list
Arguments = sys.argv[1:]

if "--encrypt" in Arguments:
    # Read in lines from either: file, or input()
    Messages = []
    # Call the encryption function on each message (line)
    # ...
    # Print each encrypted message
    # ...

elif "--decrypt" in Arguments:
    # Read in lines from either: file, or input()
    Messages = []
    # Call the decryption function on each message (line)
    # ...
    # Print each decrypted message
    # ...

else:
    print("Please provide instructions for this program:")
    print("--encrypt [message, --file FileName] : encrypt message or the contents of FileName.")
    print("--decrypt [message, --file FileName] : decrypt message or the contents of FileName.")
    print("Where [...] are optional arguments.")

