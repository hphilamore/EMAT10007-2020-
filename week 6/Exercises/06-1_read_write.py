#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:49:05 2020

@author: hemma
"""
# WRITE


file = open("scores.txt", "w")

text = "John 15"

# print(file.closed)

file.close()

print(file.closed)

# --------------------------------------------

text = "Hemma 33"

file = open("scores.txt", "w") # write

file.write(text + "\n")

file.close()

# --------------------------------------------


text = "Farhad 44"

file = open("scores.txt", "a") # append

file.write(text + "\n")

file.close()

# --------------------------------------------

5r

# --------------------------------------------


file = open("scores.txt", "a")
    
for k, v in scores.items():
    file.write(k + str(v) + "\n")

file.close()

# --------------------------------------------

# READ

file = open("scores.txt", "r")

names = []
scores = []

for line in file:
    #print(line, end="")   
    i = line.split()
    #print(i)
    names.append( i[0] )
    scores.append( int(i[1]) )

file.close()
  
#print(scores)
    
index = scores.index( (max(scores)) )

print("highest score player: " + 
      names[index] +
      "\n player scored " + str(scores[index])
      )

# --------------------------------------------

file = open("scores.txt", "r")

for line in file:  
    i = line.split()
    print(i)

file.close()
  
# --------------------------------------------



# AUTO CLOSE

# file = open("scores.txt", "a")
# file.write("Lisa 50 \n")
# file.close()

with open("scores.txt", "a") as file:
    file.write("Lisa 50 \n")
    file.write("Zoe 50 \n")
    file.write("Ben 50 \n")
    
a = 1

# --------------------------------------------

# READ & WRITE


new = "Tim 87"

with open("scores.txt", "r+") as file:
    
    file.write(new + "\n")

    names = []
    scores = []
    
    for line in file:
        print(line, end="")   
        i = line.split()
        #print(i)
        names.append( i[0] )
        scores.append( int(i[1]) )

# file.close()
  
print(scores)

    
index = scores.index( (max(scores)) )

print("highest score player: " + 
      names[index] +
      "\n player scored " + str(scores[index])
      )





















