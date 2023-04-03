# Create list
"""
name_List =["Vishali","Tharanya","Kavya","Manisha"]
# Assign a variable of list
# Using iter method 
Names =iter(name_List)
# Print the value of list in (next keyword) using.
print(next(Names))
print(next(Names))
print(next(Names))
print(next(Names))
"""
# Using for loop 
"""
for i in Names:
    print(i)
"""
"""

#  Create a class
class itertors_List:
#  Create an iter method 
  def __iter__(self,name ,age ,city,salary):
    self.Name =name
    self.Age =age 
    self.City =city
    self.Salary =salary
#  Return type is must   
    return self,name,age ,city,salary
  def __next__(self):
     assign=self.Age,self.City,self.Name,self.Salary
     self.Age +=1
     return assign
  
#  Create a object
newobj=itertors_List()
myiter = iter("kavin","25","chennai","20000")
myiter =iter(newobj)
print(next(myiter))
"""


#  Create a class
class sequnce_number:
  def __iter__(self):
    self.no = 1
    return self

  def __next__(self):
    assignig = self.no
    self.no += 1
    return assignig

my_obj = sequnce_number()
iterlist = iter(my_obj)

print(next(iterlist))
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))

print(" Stop iteration ")
class stop_iter:
  def __iter__(self):
    self.values= 1
    return self

  def __next__(self):
    
    if self.values <= 10:
      store = self.values
      self.values += 1
      return store
    else:
     raise StopIteration

stopiters = stop_iter()
myiter = iter(stopiters)

for store in myiter:
  print(store)


  
  






