#  ordered and unchangeable and round brackets must allow dublicats values
#  index stated 

unchange =("land","place","city","village")
num =(10,20,30,20)
print(num + num)
print(len(num))
print(unchange)

#  create tuple
ttype =("oneideam")
type2 =("one ideam and camma means lets cuntinue",)
print(type(ttype))
print(type(type2))


#  data type
s =("name","vishli")
n =(1,2,3,4,5,6)
b =(True,False)
print(type(s),type(n),type(b))
print(s,n,b)

# all datatype is store in tuple 
dd =("words",22,20.4,True)
print(dd)

#  constructor
aa =tuple(("apple","ornge","mango","banana"))
print(aa)
print(aa[1])
print(aa[-1])
print(aa[-4:-1])
print(aa[1:3])
print(aa[:4])
print(aa[2:])
print(aa[:])

# check if condition
li =("papper","pen","ink","note")
if "pen" in li:
    print("yes e char is pressent")
else:
    print("no its not present ")   

# tupls update 
x =(1,2,3,4,5,6) 
y =list(x)
y[1]=100
y.append(299)
x=tuple(y)
#  print(y)
print(x)    

# tuple  to tuple adding 
aa =("ani","mani","kabi")
bb =("pavi",)
aa +=bb  
#aa = bb+aa
print(aa)
#print(aa+bb)

#remove 
k =(10,11,12,14,15)
j =list(k)
j.remove(10)
#  j[2]=k                           2 time adding
j.pop(2)
k=tuple(j)
print(k)

# del 
# thistupl = ("apple", "banana", "cherry","apple")
# del thistupl
# print(thistupl)

print(" thistupl was deleted so error accour")

#unpacking 
#  we can create normal tuple is called packing  
tu =("apple", "banana", "cherry","apple")    # packing 
(green,yellow,red,black)=tu
print(green,yellow,red,black)

pl =("animls","birds","trees","water","land")
(cat , peacock ,* white)=pl
print(cat)
print(peacock)
print(white)

le=("cat","dog","camal","lion","tiger")
(ct,dg,*cl,tr)=le
print(ct,dg,cl,tr)

#loop 
tpl =("sun","moon","star","air","fire")
for i in tpl:
    print(i)

var =("sun","moon","star","air","fire")
for x in range(len(var)):
    print(x,var)
    print(var[x])

atuple =("monday","tuesdy","wednesday","thursday","friday","saturdy","sunday")
i =0
while i <len(atuple):
    print(atuple[i])
    i=i+1
    
#join tuple 
alpha =("A","B","C","D")
numeric =(1,2,3,4)
merge =alpha + numeric
print(merge)

alphabet =("a","b","c","d")
nume = alphabet + (5,6,7,8)
nume1 = alphabet *2
print(nume)
print(nume1)

# count
counting =(1,1,2,4,56,57,88,88,88,99,00,55,67,4,56,"vishali", "vishali","thara")
#  u = counting.count(88,"vishali")
u = counting.count(88)                                                  #888 -----0
print(u)