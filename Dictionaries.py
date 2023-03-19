# ordered changeable store pair key and value ideam 
student ={
    "name" :"ramya",
    "age" : 21,
    "id"  :202
}
print(student)

student ={
    "name" :"ramya",
    "age" : 21,
    "id"  :202
}
print(student["name"])            #key  using 

# cant allow duplicate key values
student ={
    "name" :"ramya",
    "age" : 21,
    "id"  :202,                       #??????
    "id" : 2001
}
print(student)

#len
student ={
    "name" :"ramya",
    "age" : 21,
    "id"  :202,                       #duplicate key and value can't count 
    "roll no" : 203
}
print(len(student))

# type 
student ={
    "name" :"ramya",
    "age" : 21,
    "id"  :202,                                    # all datatype accepted
    "roll no" : 203.0,
    "lis" :["anu", True,22, 66.0, "a"],
    "dupl":("kavi",22,44,90,True,"b"),
     "myset" : {"apple", "banana", "cherry"}
}
print(type(student))

#Constructor
student =dict(name ="ramya",age = 21,id =202)   

print(student)

#Access Dictionary Items
student ={
    "name" :"ramya",
    "age" : 21,
    "id"  :202,                      
    "roll no" : 203
}
veriable = student["age"]            #key name  access inside squre brakcets
print(veriable)

student ={
    "name" :"ramya",                 # using get method in keyname access
    "age" : 21,
    "id"  :202,                      
    "roll no" : 203
}
x=student.get( "roll no")
y=student.get( "address")                    # invailed keyname is returen ( none )                                           
print(x)
print(y)

# add 
student ={
    "name" :"ramya",                
    "age" : 21,
    "id"  :202,                      
    "roll no" : 203
}
print(student)     #before  add 
student["class"]="A"
print(student)     # affer add 
z = student.keys()                                #    all key name is visible here
print(z)

v =student.values()                                # all values are visible here
print(v)

#change in the original dictionary
student["class"]="b"
print(student)
"""
#add a new  ideam in  original dictionary
student ["class teacher"]="techers"
print(student)
i=student.items()                                   # all idems  visible this method
print(i)
student["class teacher"]="malar"
print(student)
if "vishali " or "age" in student:
    print("yes is value is pressent")
else:
    print("no this value is not present")

#change values
ChangeValue = {
  "brand": "RE",
  "model": "bullect 350",
  "year": 1964,
 
}
print( ChangeValue)
ChangeValue["year"] = 2018
print(ChangeValue)

ChangeValue = {                                         #update method
  "brand": "RE",
  "model": "bullect 350",
  "year": 1964
}
ChangeValue.update({ "year ": 2023})
print(ChangeValue)


#add new value 
ChangeValue["current model"]="650cc"
ChangeValue.update({"add new ":"bike"})
print(ChangeValue)

# removing ideam pop() key and value remove pair this condition
group ={
    "name ":"vishali",
    "elder sister name":"Tharanya",
    "yonger sister name ":" pirliya",
    "new name add":"kavya"
}
group.pop( "name ")
print(group)

# random item is removed popideam()
group.popitem()
del group["elder sister name"]
group.clear()
#  del group   totally del
print(group)

#loop
ChangeValue = {
  "brand": "RE",
  "model": "bullect 350",
  "year": 1964,
 
}
# only loop key name 
for i in ChangeValue:                               
    print(i)

for i in ChangeValue.keys():
    print(i)

# only loop value name 
for i in ChangeValue:
    print(ChangeValue[i])   

for i in ChangeValue.values():
    print(i)

#keys and values, by using the items()  
for i ,L  in ChangeValue.items():
    print(i,"  ", L)

#Copy Dictionaries    
mydice ={
    "fname":"fristname",
    "lname":"lastname",
    "cname":"confirmname"
}
newdice =mydice.copy()
print(newdice)

newdice=dict(mydice)
print(newdice)

#  Nested Dictionaries
# one dict cn contain dict
"""
my_class={
    "10th":{
    "tamil":"mark",
    "english":"mark,"
    },

    "11th":{
    "account":"accmark",
    "economic":"ecomark",
    },
    "12th":{
    "computer":"cp mark",
    " maths":"mat mark"
    }
}
print(my_class)

class10th={
    "tamil":"mark",
    "english":"mark,"
    },
class11th={
    "account":"accmark",
    "economic":"ecomark",
    },
class12th ={
    "computer":"cp mark",
    " maths":"mat mark"
    }
singledict ={
    "ten":"class10th",
    "leventh":"class11th",
    "twelth":"class12th"
}
print(singledict)

# access 
print(my_class["10th"]["tamil"])
#print(my_class)
