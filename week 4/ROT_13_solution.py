Key = {
	'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m',
	'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'
	}

def EncodeDecode(Message):
	"""
	First we generate a list of characters (strings) by passing in the Message
	string as an argument to the list() function. We do this because strings
	are immutable, and so we cannot directly change the characters in the string.
	We can, however, replace items in a list.

	Notice that to make an empty list, we can write:
	Message = []     or     Message = list()
	But to make a list from a string, we need to use the function list().
	"""
	Message = list(Message)
	# Similarly for a string, we could have written:
	# Output = ""
	# which is an empty string.
	Output = str()

	for Letter in Message:
		# Firstly, we want to check for spaces and any other characters not in Key
		# that we do not want to replace.
		if Letter not in Key.keys():
			# If the character isn't in Key, keep it the same.
			Output += Letter
		else:
			"""
			+= is a contraction of x = x + ...
			so that we can just write x += ...

			We provide the index as the letter we currently have in our message
			in order to get back the letter we want to replace it with, according
			to the mapping of letters in the Key list.
			"""
			Output += Key[Letter]

	"""
	By RETURNING the output, rather than printing it, we can do additional things
	with the encoded/decoded message. Of course, we can print it out later, as usual,
	but we can also supply the output of the EncodeDecode() function to another call
	to EncodeDecode().
	"""
	return Output

MyMessage = "Hello world!"

# print the message
print(MyMessage)
# print the encoded form of the message
print(EncodeDecode(MyMessage))
"""
print the decoded form of the encoded message as follows:
DECODE ( ENCODE ( MYMESSAGE ) )
Because the ROT-13 cipher is symmetric, the output of one function can be the
input of another function. The magic of using RETURN instead of just printing
from the function!
"""
print(EncodeDecode(EncodeDecode(MyMessage)))
