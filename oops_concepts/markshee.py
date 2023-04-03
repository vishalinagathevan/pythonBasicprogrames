print(" STUDENT MARK STATEMENTS ")
# Difine a function
# Used to input function get the student name
def student_Name():
    name =str(input("Enter the student name : "))
    print("Student Name is :-",name)
student_Name()    

# Difine a function
#  Used to input function get the student roll no
def student_RollNo():
    roll_no =int(input("Enter your Rollno :"))
    print ("Student Age is :-",roll_no)
student_RollNo()

# Difine a function
# Used to input function get the student subject
def Student_subject():
      tamil =int(input("Enter the first mark : "))
      english =int(input("Enter the second mark : "))
      maths =int(input("Enter the third mark : "))
      science =int(input("Enter the fourth mark : "))
      social =int(input("Enter the fiveth mark : "))

# Marks totel
      totel= tamil+ english + maths + science + social  
      print("Student Totel Marks :-",totel)  
# Avarge the totel marks      
      avarge = totel/5
      print("Avarge is :-", avarge)

Student_subject() 
     