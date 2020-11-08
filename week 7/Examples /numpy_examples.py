import numpy as np


# constructing a vector from a list
# Note that the actual class is ndarray!
# array is used as a way to initialise ndarrays

a = np.array([1,2,3,4])
# defining the type of number
b = np.array([1,2,3,4], dtype=np.float)  # other types are np.int and np.complex

print(type(a))
print(a)
print(b)


# making matrices
print("matrix")
# nested lists
A = np.array([[1,2,3],[4,5,6]])
print(A)

print("--> zeros")
# initialise array with zeros
a = np.zeros(5)     # vector of five zeros
b = np.zeros((3,5)) # 3x5 matrix, (3,5) as tuple!

print(a)
print(b)

print("--> random.rand")
# initialise array with random numbers
c = np.random.rand(2,5)
print(c)


print("--> arange")
# from "a range" - similar functionality as built-in range()
a = np.arange(3)  # [0,1,2]
print(a)
b = np.arange(2,5)  # [2,3,4]
print(b)
c = np.arange(0,100,2) # (start,stop,step)
print(c)


# =========================================

print("--> reshape")
a = np.arange(6).reshape((3, 2))
print(a)
print(a.reshape(2,3))
# making ma

# using list comprehension to make interesting vectors
time = np.arange(0,10,0.01)
y = [x*2+1 for x in time]
a = np.array(y)
print(a)


#========================================
print("Example of matrix manipulation:")

A = np.random.rand(2,2)
print("A: \n" + str(A))
print("Transpose: \n" + str(np.transpose(A)))
print("Eigenvalues: \n" + str(np.linalg.eig(A)))
print("Inverse: \n" + str(np.linalg.inv(A)))
print("Determinate: \n" + str(np.linalg.det(A)))
print("Rank: \n" + str(np.linalg.matrix_rank(A)))
print("Size: \n" + str(A.size))      # also np.size(A)
print("Shape: \n" + str(A.shape))    # also np.shape(A) → tuple!

B = np.array([[1,2],[3,4]])
C = np.array([[-3,1],[5,-2]])
print("B: \n" + str(B))
print("C: \n" + str(C))
print("B+C: \n" + str(B+C))
print("B*C: \n" + str(B*C))


#========================================
print("Slicing your arrays")

# accessing sub parts of matrices
# start:stop:step
A = np.arange(12).reshape(3,4)
print(A)
print("First row: \n" + str(A[0,:]))
print("First col: \n" + str(A[:,0]))
print("Submatrix 1: \n" + str(A[0:2,0:2]))    #[0 1][4 5]
print("Submatrix 2: \n" + str(A[1:3,1:2]))   #[[5][9]]

