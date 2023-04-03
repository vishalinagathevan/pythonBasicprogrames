# Create a class
class phone:
    # Create __init__method
    print("SUPER CLASS ")
    print()
    def __init__(self,color,price):
        self.color =color
        self.price =price

    # Create normal method
    def models(self,oppo,vivo,apple):
        self.oppo =oppo
        self.vivo= vivo
        self.apple =apple
    #  Create display method 
    def display (self):
        print("Mobile Color : ",self.color)
        print("Mobile price : ",self.price)  
        print("First model is : ",self.oppo)
        print("second model is : ", self.vivo)
        print("Third model is : ",self.apple) 

# Create object in class 
android =phone("Black",12000)
android.models("Oppo","Vivo","Apple")
android.display()

# Inherite the parent class
# Child child class
print()
print("CHILD CLASS")

class Laptop(phone):
    pass
# Create an object only child class 
lap =Laptop("white",15000)
lap.models("Hp","Apple","Thinkpad")
lap.display()
