#  String dadatype  only latters
word ="collection of character its called string within single qouats or double qouats its must. "
word1 ='i am vishali'  #  'i'm fine'
print(word , word1)
print(type(word),type(word1))

#  integer datatype  no need single qouats or double qouats integer is only numbers,
a = 10
b = 20
print(a+b,type(a),type(b))

# float this datatype is only point numbers stored 
no =1.5
no1 =2.10
print(no+no1)
print(type(no),type(no1))

# complex datatypes number and latter merged 
com =1j   #only used for j char.
com1 =4j
print(com +com1)
print(type(com),type(com1))

# list - allows dupicates values and orderd secequance  []-sysbol
# list usage is one variavle we can store many valaues in diffrent datatypes.
furits=["apple", "banana",77, "cherry","apple"]
animal =["cat", "tiger", 2.0,"cow","dog","tiger"]
print(type(furits))
furits.append("orange")
furits.append("pinapple")
furits.reverse()
print(furits+["apple", "banana", "cherry","apple"]) # add list +list
print(len(furits+animal))
print(furits+animal)

# tuple -tuples diffrent datatypes we can store and can't modified  and orderd list ()-this is tuple sysbol
student=("vishali",22,"maduri","kavi","maduri")
print(student.__sizeof__) #  hwo  to use it?
print(student)

# range 
x=range(7)
print(x)

#  dict key and value store in {} place  for example key is immutable but value is muteable 
#  key name  value vishali  
dict={"name" :"nagathevan","age" :52,"mother name":"pappa","age1" :45}  #  and{"mother name":"pappa","age1" :45}
print(dict.get("name"))
print(dict.get("age"))
print(dict.get("age1"))
print(dict.get("mother name"))

# set -unordered list  dont allow dublicates value {} allows any datatype 
colours ={"green","red","blue","red","yellow","green",66,67.99}
print(colours.add(88))
print(colours.add("white"))
print(colours.remove("green"))
print(colours)
#print(colours+animal) # set ,list, tuple  cant merge 

# frozenset -set also same but frozenset cant add new data this is only diffrence.
group =frozenset({"a","b","a","c","d","d"})
#print(group.add("e"))
print(group)

#boolen only true or flase
x=1
if 1 < 10:
    print("yes")
else:
    print("no")    

# byte immutuable
by =bytes(10)
print(by)

# bytearray muteable
byt =bytearray(10)
print(byt)



