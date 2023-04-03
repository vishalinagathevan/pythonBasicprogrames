
#  Difine a class
class Laptop:
#  Difine a in _build function 
   def __init__(self,name, cost,hdd,ram):
      self.Name =name
      self.Cost =cost
      self.Hdd =hdd
      self.Ram =ram

#  Create a object in CLASS LAPTOP
laptop =Laptop("Windows",50000,512,8)
print("The details of the loptop :: ")
print("Name : ",laptop.Name)
print("Cost : ",laptop.Cost)
print("Hard Disk Capacity : ",laptop.Hdd)
print("Ram : ",laptop.Ram)    
print()    
"""
#  Difine a class
class Mobile :
# Create a init method    
   def __init__(self, name ,price, model, color) :
      self.Name =name
      self.Price =price
      self.Model =model
      self.Color =color
# Create a string  method
   #def __str__ (self):
     # pass
      #return f"({self.Name},{self.Color},{self.Model},{self.Price} )"   
# Create display method 
   def display (self):
      print(" Display the methods : ")
      print("MObile Name  : ",self.Name )
      print("Mobile Price : ", self.Price )
      print("Mobile Model : ",self.Model )
      print("Moble Color  : ",self.Color)
         
#  Create a object      
mobile =Mobile("OPPO",11000,"purpul","AS3")
#  print(mobile)
mobile.display()
print()

#  Create a default value in __init__ method
#  Create a class
class Dog :
      print(" Print the default parametter. ")
# Create a init method   
      def __init__(self,dog_color="Black",dog_name="Jiyamu") :
          self.DogColor=dog_color
          self.DogName =dog_name
#  Create a object
dogs =Dog()  
print(dogs.DogColor)
print(dogs.DogName)  
print()     
"""
#  Create a class without __init method
class bank:

    def Accound_creater(self, name ,account_no):
        self.name =name 
        self.account_no =account_no

    def  details_OfAcc(self,branch_name,ammount):
        self.branch =branch_name
        self.amount =ammount

    def view_Result(self):
        print("Customer Name is : ",self.name)
        print("Account Number : ",self.account_no)
        print("Branch Name  : ",self.branch)
        print("Amount : ",self.amount)

#  Create a class object
Bank =bank()
Bank.Accound_creater("Anu",26841000)
Bank.details_OfAcc("Madurai","20000")
Bank.view_Result()
         









