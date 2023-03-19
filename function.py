#  function name calling 
"""
def display():
  print("display the value")  
display()
print()


# extra and less value cant consiter
def add(a,b):
  print("add function using in parametter : ",a+b)
  #  return 
add(5,10) 
add(10,20)   
print()

def sub (x,y):
  return x-y
print(sub(10,2))
print()

#  number of aruguments
def view (name ,age ,city):
  print("view function printed :")
  print("name:"+ name + "  " +" age:" + age+"  "+ "city:" + city)
view("vishali","22","madurai") 
print()

def view (name ,age ,city):
   return age
print(" i will get on one value from returen type using. ")
print(view("anu","25","chennai"))         #????????????
print()

def view (name ,age ,city):
 print("function excepts  correct number of  arguments not more and less value ")
 return("name: "+ name + "  " +" age: " + age+"  "+ "city: " + city)
print(view("Tharnya","24","chennai"))
print()
"""
def fun (A1,A2,A3):
   print("key value :"+A1)
   fun(1,"two","three")                  # NUMBER ????


def sing (**single1):
  print("dictionaries value:"+ single1[ "leventh"])
sing(ten ="class10th",leventh ="class11th",)  # key value is must ???

#Default Parameter Value
def myclass(std ="100"):
  print("stmarks:"+std)
myclass("50")
myclass()
myclass("90")  

def mul(aa , bb):
 return(aa*bb,aa +bb,aa/bb)
print(mul(10,2))
print()

#  Arguments, *args
def number_of_arguments(*players):
  print("do not know ....how many arguments.at the time  add a (*) before the parameter name ")
  print("players name :",players[1])
 # print("invlied arguments pass :",players[5])            (out of range an error )
number_of_arguments("kavin","bala","sathya","varun")  
print()

# keyword arguments
def keyword_argument(father,mother,son):
  print("keyword arguments printed")
  print("Son name : ",son)
  print("Father Name : ",father)
  print("mother name : ",mother)
keyword_argument(mother="bavani",son="sakthi",father="deva")  
print()

def my_function(child3, child2, child1):
  print("not use keyword argument ")
  print("The youngest child is : " + child3)
  print("The youngest child is : " + child1)
  print("The youngest child is : " + child2)
my_function("mohi", "kirish", "veera")
print()

#keyword arguments is unknown ** add a before prametername
def function_name(**member):
  print("double star using:")
  print("she name is : ",member["name"])
  print("she is ",member["age"]," years old.")
function_name(name ="pavana",age = 24,city ="madurai") 
print() 

print("Default Parameter Value")
def greetings(whises ="great day!"):
  print(whises," Thank you")
greetings("Happy birth day.")  
greetings()
print()

print("Return Values")
def fun(i):
  return 2 +i
print(fun(7),fun(10))

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
def key(lock):
  for i in (lock):
    print(i)
slist =["home key","room key","peivate key","public key", "common key"]    
key(slist)