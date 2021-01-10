import math 

# First, take input from the user in the form of the x and y coordinates of the point to test. 
# Note that here, we are not implementing checks on the input, and trusting that the user will input numbers. 
# (A sometimes dangerous assumption!)

x = input('Please input the x coordinate of your point.')
y = input('Please input the y coordinate of your point.')

Point = (int(x),int(y))

# Next, we define the circles as given by the exercise with their centre and radius

CentreC1 = (0,0)
CentreC2 = (2,1)
CentreC3 = (-5,0)

RadiusC1 = 5
RadiusC2 = 2
RadiusC3 = 3

# Here we calculate the Euclidean distance from the point given to each of the circle centres. 

DistanceToCentreC1 = math.sqrt((Point[0]-CentreC1[0])**2+(Point[1]-CentreC1[1])**2)
DistanceToCentreC2 = math.sqrt((Point[0]-CentreC2[0])**2+(Point[1]-CentreC2[1])**2)
DistanceToCentreC3 = math.sqrt((Point[0]-CentreC3[0])**2+(Point[1]-CentreC3[1])**2)

print(DistanceToCentreC1)
print(DistanceToCentreC2)
print(DistanceToCentreC3)

# Finally, we test if the distance of the point to the each circle's centre is smaller than that circle's radius.
# If so, the circle contains the point and we print the appropriate message. 

if DistanceToCentreC1 <= RadiusC1:
    print("The point " + str(Point) + " is in circle C1.")
else:
     print("The point " + str(Point) + " is NOT in circle C1.")
        
if DistanceToCentreC2 <= RadiusC2:
    print("The point " + str(Point) + " is in circle C2.")
else:
     print("The point " + str(Point) + " is NOT in circle C2.")

if DistanceToCentreC3 <= RadiusC3:
    print("The point " + str(Point) + " is in circle C3.")
else:
     print("The point " + str(Point) + " is NOT in circle C3.")
        
        
        
