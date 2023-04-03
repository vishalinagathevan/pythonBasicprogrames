"""
#  The variavle only available in inside function 
#  Create a function 
def pan():
    pan_no = 67495
    print("This is pan-card number : ",pan_no)
# Function calling 
pan()   

# This variable used to outside the function .
# print("Pan_no is not difine",pan_no)

# Function inside function
#  Create a function 
def pan():
    pan_no = 123
    def inside_pan():
     print("This is pan-card number, Used to inside fun : ",pan_no)
# Function calling
    inside_pan()
pan()  

# Goble variable 
customer_Name="vishali"
customer_Age =21
#  Difine a function 
def aadhar():
#  Used to local variable and global variable .   
   aadhar_NO =1294
#  Local variable 
   print("AADHAR NUMBER IS : ",aadhar_NO)
#  Global variable   
   print("AADHAR CARD OWNER NAME IS : ",customer_Name)
#  Function calling    
aadhar()
#  Used to global variable in outside the function.
print("AADHAR CARD OWNER AGE IS : ",customer_Age)     

"""
#  Naming variable 
#  Create a global variable 
apple_price =200
#  Difine a function
def price():
   # Create a local function.
   apple_price =150
   print("First time it will print local variable : ",apple_price)
price()
print("Second time gobal vriable is printed : ",apple_price)   


# Global keyword 

def global_keyword():
   global no
   no=10  
   global_keyword()   
#  print(no)
"""

no=100
def global_keyword():
   global no
   no=10
   print(no)
global_keyword()   
print(no)

no=120
def global_keyword():
   global no
   no=10
print(no)   
global_keyword()   
print(no)

"""
