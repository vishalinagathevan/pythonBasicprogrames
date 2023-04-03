# create a class 
# use the class kewyword .
class Student:
# create any variables    
    number =100
# use the class named Student to create objects:
obj =Student()
# used to objecte name (.) call the varibales.
print('Property of number in student class')
print(obj.number)    
print()

# create a class ,class named MyClass
print("Used to __init__ function ")

class MyClass:
# used __init__() function to assige a values
     def __init__(self,name ,age ,city ) :
         pass
#  create a onjecte in myclass objecte named Information
Information =MyClass("vishali",22,"madurai")  
print("Pass Statement Using:",Information)  
print()

# create a class ,class named MyClass
class MyClass:
# used __init__() function to assige a values
     print("__init__ function ")
     def __init__(self,name ,age ,city ) :
          self.Student_name =name
          self.Student_age =age
          self.Student_city =city

#  create a onjecte in myclass objecte named information
information =MyClass("vishali",22,"madurai") 

#  To called function  used in objecte (.) function name.  
print('Student name:',information.Student_name)
print ('Student age:',information.Student_age)
print()

# create a new class
class Car:
# variable initiated.
  #   Value_1 =None
   #  Value_2 =None
     def __init__(self,X_Val=1,Y_Val=2):
        self.Value_1=X_Val
        self.Value_2 =Y_Val
        print("automatic calling __init__ function  ")
#  create a objecte name in current class ,objecte named NewCar
NewCar =Car(20,30)
print(NewCar.Value_2,NewCar.Value_1)
print()

# without using str function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
info = Person("janani", 16)
print(info)

print("with using str function")
class Member:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
      return f"{self.name},{self.age}"

obj= Member("abi", 26)

print(obj)         
     
class Create:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
      return self.name

OBJ= Create("abi", 26)

print(OBJ)      

# normal class create
class School:
   def Teachers(i):            #?????? self
     print("High School Teacher")
#  create a objecte
HM =School()
HM.Teachers()

class Vishali:
   def info (self,name,age):
      self.n =name
      self.a=age
      print("my name is",self.n )
      print("my age is",self.a)
x =Vishali()
x.info("raja",22)

#
print()
class Employee:
   
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
  
   def display(self,age):
     self.Age =age

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary,"Age : ",self.Age)
objects =Employee("Vishali",10000)
objects.display(22)
objects.displayEmployee()

print()
class Employees:
   
   def __init__(self):
     print("222")
  
   def view (self,age):
     self.age =age
     print (self.age)
Work =Employees()   
Work.age(21)  








