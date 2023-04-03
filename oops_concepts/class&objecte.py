#  Create a Super class 
class Animal :
    def __init__(self,dog,cat):
        self.Dog =dog
        self.Cat =cat
    def display(self):
         print("Dog : ",self.Dog)
         print("Cat : ", self.Cat)   

# Create object  only child class
ani =Animal("Attack","eat")
ani.display()







  
    











