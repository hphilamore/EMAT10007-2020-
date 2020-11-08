def FillVerses(Number):
    """
    Recursive solution for BottlesOfBeer

    The way recursion works is by calling a function from within itself, going
    as many layers deep as is necessary. This means that the function only returns
    a result when the final function call meets some condition and does not call
    itself, instead returning its result back to the function which called it.
    Therefore we must deal with such "edge cases". In this example, when there are
    no more bottles of beer left on the wall, we just return an empty list to add to
    the rest of the lists.
    """

    if Number == 0:
        return []

    BottlesOfBeer = [
        f"{Number} bottles of beer on the wall, {Number} bottles of beer.\n"
        f"Take one down, pass it around, {Number} bottles of beer on the wall."
    ]

    return BottlesOfBeer + FillVerses(Number - 1)

Bottles = FillVerses(100)
for Bottle in Bottles:
    print(Bottle)
