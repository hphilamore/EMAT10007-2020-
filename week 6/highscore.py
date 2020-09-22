# high score table
#highScoreTable = [ [345,"Janice Waterfell"],[301,"Clement Durage"],[240,"Anthony Chargrin"]]
# read in the high score
HighScoreTable = []
MyFile = open("HighScoreList.txt","r")
for Line in MyFile:
    if(Line !=""):
        Line = Line.strip()
        EntryList= Line.split(',')
        HighScoreTable.append( [int(EntryList[0]),EntryList[1]] )



# check if new player made it into the high score
# checkout the get the last element using -1 and the first with 0
LowestScore = HighScoreTable[-1][0]
if NewScore >= LowestScore:
    print("Congratulations you made it into the highscore")
    NewEntry = [NewScore, NameOfPlayer]
    HighScoreTable.append(NewEntry)
    HighScoreTable.sort(reverse=True)
    HighScoreTable.pop()
else:
    print("Sorry you did no make it into the highscore")

# print the current table
Counter = 0
for Entry in HighScoreTable:
    Counter += 1
    print(str(Counter) + ": " + Entry[1] + " with " + str(Entry[0]) + " points ")

# Close file so other programms can access it
MyFile.close()

