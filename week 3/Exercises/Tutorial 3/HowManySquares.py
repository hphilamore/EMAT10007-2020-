# How many squares do we have to add up to exceed 1e6?
# (An illustration of a while loop)

cumulativeSum=0
counter=0

while cumulativeSum<1000000:
    counter+=1
    cumulativeSum=cumulativeSum+(counter**2)
    print(counter,cumulativeSum)
print("The answer is", str(counter))
# Note we had to use str() to convert the counter (of type int) into a string type.

# Note that we can use also a comma to join strings
# What is the difference when you join them with a plus sign?

# add a line that shows the results for every step of the while loop
