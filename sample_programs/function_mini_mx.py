# Create a sequence list and find the minimum and maxcimum value
# Using in-build function 

Mini_max=[10,21,1]
print("Minimum Value Of The list:",max(Mini_max))
print("Maxcimum Value of The List:",min(Mini_max))

#  Create an one sequence list

def max_min(data):
  large = 0
  small= 0 
  for num in data:
    if num > large : #???
      large = num
    elif num < small:
        small = num      #???
  return (large,small)
#  no_list =[-1,90,2,10,2,70]
print(max_min([-1,90,2,10,2,70]))



