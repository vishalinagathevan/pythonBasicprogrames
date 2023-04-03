# takes a positive integer and returns the sum of the cube.
#  Create a mothod 
def sum_of_cubes(number):
# Using while loop
 number -= 1
 total = 0
 while number > 0:
  total += number * number *number
  number -= 1
 return total
print("Sum of the cube smaller then specified number : ",sum_of_cubes(4))  

