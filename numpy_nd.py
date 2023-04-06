#  Numpy is installed .
#  Import numpy it changed the name of np .
import numpy as np
Array_list =np.array([1,2,3,4,5])
print("Numpy is impored and ready to use :- ",Array_list)

# checking  Numpy version.
print(np.__version__)
print(type(Array_list))

#  Use a tuple to create a NumPy array
Array_tuple =np.array([1,2,3,4,5])
print(" Tuple converted into an ndarray :- ",Array_tuple)

# 0-D Arrays
# I think single open and open brackets only using .
array_0D =(88)
array_ch =("vishali")
print(" Zero D array : ",array_0D)
print(" Zero D array  with character or words : ",array_ch)

# Uni-dimensional or 1-D array.
# Normal basic  array
ar = np.array ([1,2,3])
print("Basic array : ",ar)

# 2-D Arrays 
# One D array is must. row and coloumn 
ar1 = np.array ([[1,2,3],[1,2,3]])
print("2 D array : ",ar1)

# Create a 3-D array with two 2-D arrays, both containing two arrays 
ar2 = np.array ([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3 D array : ",ar2)

#  Check Number of Dimensions
print("Basic array",ar.ndim)
print("3 D array",ar2.ndim)


#  NumPy Array Indexing 
#  Access Array Elements
ar = np.array ([1,2,3,4])
# Zero mean first position .
print(ar[0])

# Adding arrays
print("Adding 2 index number based : ",ar[0] + ar[2])

# 2nd element on 1st row
ar1 = np.array ([[1,2,3],[1,2,3]])
print(" 2 D array 2nd element on 1st row : ",ar1[1,1])

#  Negative Indexing
print(" 2 D array 2nd element on last row : ",ar1[1,-1])

#  NumPy Array Slicing
ar = np.array ([1,2,3,4])
print("Slicing the list : ",ar[1:2])

#  Slicing the list only start position
print("Slicing the list only start position  : ",ar[1:])

#Slicing the list only end  position
print("Slicing the list only end position  : ",ar[:3])

#  Negative Slicing
print("Slicing the list only negative value  : ",ar[-3:-1])

# STEP method using 
print(" Step method  : ",ar[1:3:2])

# Step method  using 2 D array
ar1 = np.array ([[1,2,3],[1,2,3]])
print(" Step method  using 2 D array : ",ar1[0:2, 1:4])