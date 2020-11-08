Mult3 = "Fizz" 
Mult5 = "Buzz"
Limit = 0
Limit = int(input())
for i in range(1,Limit+1):
    if i% 15 == 0:
        print(Mult3+Mult5)
    elif i%3 == 0:
        print(Mult3)
    elif i%5 == 0:
        print(Mult5)
    else:
        print(i)


