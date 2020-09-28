def FillVerses(Number):
	"""
	EXTENSIONAL EXERCISE
	--------------------
	Fill a list of verses, and return the list in descending order, using whichever method you'd like.

	For example, after filling the list below, I reverse the list when I return it.
	But you could reverse the range() function in the list comprehension, or sort the list in reversed order using sorted(...,reverse=True).

	The list comprehension follows the general pattern of:
	[x for x in range(n)] to fill a list with the numbers 0 .. n-1.
	You can look up additional examples of list comprehensions online - they're really
	useful for quickly generating lists. You can even add conditions like so:
	[x for x in range(n) if x % 2 == 0]
	which fills a list with even elements only, and will produce the following list:
	[0, 2, 4, 6, 8, ..., n - 2]
	"""
	BottlesOfBeer = [
		"{0} bottles of beer on the wall, {0} bottles of beer.\n".format(str(x)) + \
		"Take one down, pass it around, {0} bottles of beer on the wall.".format(str(x - 1)) \
		for x in range(1,Number)
	]

	# The way I have chosen to reverse the list order is to return the list
	# as the result of calling the function reversed() with the list as the
	# argument.
	return reversed(BottlesOfBeer)

Bottles = FillVerses(100)
for Bottle in Bottles:
	print(Bottle)
