# Try and except 
# Cant divided by 0 in any values
try:
    divid =100/0
    print(divid)
# Try keyword ,must be using expect.    
except ZeroDivisionError:
  print("Cant Dividing by zero in any vaues.")  
except:
    print("Enter correct number")

# Else 
try:
   print("Welcome",878)
except:
   print("Something went wrong ")
else:
   print("Nothing went wrong ")   
# Finlly will be compulsory excuded.
finally:
   print("Finished")             


try:
  file = open("Demofile.txt")
  try:
    file.write("Welcome")
  except:
    print("Something went wrong when writing to the file")
  finally:
     print("FIle Closed :", file.close())    
except:
  print("Something went wrong when opening the file")

#  Raise
negative_no = -1

if negative_no < 0:
  raise Exception ("The number is below zero")
else:
   print("This number is printed.")


