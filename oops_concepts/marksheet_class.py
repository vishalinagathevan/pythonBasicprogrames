
#  Program to calculate total and average-marksheet
class Marksheet:

    #  Initialize the variable
    def __init__(self,name,rollno):
        self.name =name
        self.rollno =rollno

    # To concantinate the string and int    
    def __str__(self) -> str:
        pass    
    #  student_Marks function
    def student_Marks(self,history,accountancy,cs):
        self.history=history
        self.accountancy= accountancy
        self.cs=cs

 # Display the output      
    def disply(self):
        print("Student Name is :",self.name) 
        print("Student rollno  is :",self.rollno)
        print("History mark is :",self.history) 
        print("Accountancy  mark is :",self.accountancy)
        print("Compute scince mark  is :",self.cs) 

#  Calculate totel and average
    def totel_averge(self):
        marks_totel =self.accountancy +self.cs +self.history
        avarge =marks_totel/3
        print("Totel Marks is : ",marks_totel)
        print("The avarge is : ",avarge) 

#  Create an object in the current class

#  To get the input for student name

no_stu =int(input("Enter the number of students in a class : "))
for i in range(no_stu):
    if i !=0:
      print("\n Next student details")  
    student_name=str(input("Enter the student name : "))
    student_rollno=int(input("Enter the student rollno : "))
    acc=int(input("Enter the Accountancy mark : "))
    his=int(input("Enter the History mark : "))
    cs=int(input("Enter the Computer mark : "))

    result =Marksheet(student_name,student_rollno) 
    result.student_Marks(acc,his,cs)
    result.disply()   
    result.totel_averge() 
       
