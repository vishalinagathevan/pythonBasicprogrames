#  Create a list
#  Used to in-build method function
Members=["abi","thara","charu","divya"]
#  Remove the first ideam in list
#  Before Remove The List
print("Before Remove The List :",Members)
Members.pop(0)
#  After remove the list 
print("After Removing The First Ideam In The List:",Members)
print()



#  Using without in-build function
#  Create a list or tuple 
vehicle =["car","bike","bus","cycle"]
print("Before remove the ideam in vehicle:",vehicle)
#  Remove first ideam
for i in vehicle:
  if i =="car":
    continue
  else:
     print(i)
#   print("Print the vehicle ideams:: ",i ,end=" ")
#   print("Print the list of vehicle",vehicle) 