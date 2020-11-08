inputwords = input()
listwords  = inputwords.split(" ")
#lengthwords = list(map(lambda x: len(x),listwords))
for i in range(10):
    print("Word:",listwords[i],"- Word length:", len(listwords[i]))