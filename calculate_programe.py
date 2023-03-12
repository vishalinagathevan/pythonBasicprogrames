# always input method take string  value 
print("1 .add")
print("2 .subtraction")
print("3 .multiplication")
print("4 .division")
print("choice of anyone method")
 
operation =input("select method ")
#while True:

if operation == "1":
    num1 =input("enter frist number:")
    num2 =input("enter secend number:")
    print(int(num1) +int(num2))

elif operation =="2":
     num1 =input("enter frist number:")
     num2 =input("enter secend number:")
     print(int(num1) - int(num2))

elif operation == "3":
      num1 =input("enter frist number:")
      num2 =input("enter secend number:")
      print(int(num1)  * int(num2))

elif operation == "4":
      num1 =input("enter frist number:")
      num2 =input("enter secend number:")
      print(int(num1) / int(num2))

else:
     print("invaild entry ")  
      
#next_calculation = input("(yes/no): ")
##  print("select operation")
#else:
 # print("Invalid Input")
 