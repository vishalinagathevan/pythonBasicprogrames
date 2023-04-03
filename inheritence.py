# Create a super class
class Super_Class :
#  Create method of Superclass
    def __init__(self, name, age):
        self.Name =name
        self.Age =age     
#  Create an object 
print("This is SUPER CLASS")
parent=Super_Class ("Nagathevan",52) 

print("Father Name : ", parent.Name)
print("Father Age :" ,parent.Age)

#  Create a child class
# inherite the parent class

class Child_Class(Super_Class):
    def __init__(self, name, age, city):
        Super_Class.__init__(self, name, age)
        self.sonName =name
        self.sonAge =age
        self.city =city
    # Create a display method    
    def  display (self): 
        print("Son Name :",self.sonName) 
        print("Son Age : ",self.sonAge)  
        print("son city :",self.city)

#  Create a child class objecte
child = Child_Class("sakthi","55","madurai")
print(child.Name)
print(child.Age)
print(child.city)
child.display()