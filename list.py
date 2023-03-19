#  list alows duplicate value ,we can store one variable in multiple values .
#  list always based index values 0,1  only add last position
mark=[50,56,76,87,77,88,77,]
print(mark[1])
mark.append(99)
#  mark.remove[4]      
print(mark)

lis=["abc", 34, True, 40, "female"]
lis.pop(3)                            #remove index number using
print(lis[0])
print(lis)

#constructor
con = list((22,44,55,66,77))    # CONSTRUCTOR
print(con)
con[1]=10 ,52
con[2:4]=15,30
print(con)

length=["words","char",45,89.8,True]
print(len(length))
print(length)

#access list
ab =["madurai","theni","selam"]
print(ab[2])

#nagative ideam
bb =["number","names","address","id"]
print(bb[-1])
print(bb)     #reverse ?

#range 
alist =[1,2,3,4,5,6,7,8,8,9,7,5]
print(alist[2:5])

print(alist[:4])

print(alist[2 :])
print(alist[:])

print(alist[-5:-2]) #nagative number

student=["abinaya","banu","kaviya","janani","nivetha"]      #if method using
if "banu"or"kaviiya" in student:                             # and or 
    print("yes this name is available")
    print(student)  
else:
    print("not availble")  

#  change ideam refer to the index number 
order =[ 100,200,300, 400,600, 700]
order.append(500)
order[0]=10
order[1:4]=["a1","a2","a3"]
order[3:4]=["vishali","tharanya"]
print(order)

#insert idem
thinks =[" soft toys","cars","animal toy","bikes toy"]
thinks.insert(2,"baby toys")
thinks.insert(-3,"fish toys")
print(thinks)

# add list idem (last)
names =["agi","mahi","savi" ]
names.append("kavi")               #  new list adding appends ideam only last position
age =[19,20,21]
names.extend(age)
print(names)                            #?
age.extend(names)
print(age)

odd =[1,3,5,7,9,8,10,21]
even=[2,4,6,8,]
#del even
even.clear()
print(even)
odd.remove(8)
odd.pop(4)
del odd[4]
print(odd)

# loop through
# zz =[1+2]
# print(zz)
xx=["pen","pencel","note","papper"]
for i in xx:
    print(i )#,end=" ")

yy =[1,2,4,5,7,8,"aa","bb"]
for j in range(len(yy)):
    print(yy+[j])    

ll =["apple","bnana","orange","mango"]
k =0
while k < (len(ll)):
    print(ll+[k])
    k=k+1

# List Comprehension  
sub=["tamil","english","maths","scince","social"] 
book=[]
for x in sub:
    if "a" in x: 
     book.append(x)
     print(book)  
    else:
        print("not present")    


table =[1,2,3,4,5,6,7,8,9,10]
tables=[]
for b in table:
 dd= b*2
 tables.append(dd)
 print(tables)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
foods=[x for x in fruits if "a" in x]      #expre
print(foods)

score =[12,55,22,99,92,57]
sc =[ex for ex in score if ex != 99]
print(sc)

no =["school","class","student","teacher","hm"]
no1=[n for n in no]
print(no1)

new =[i for i in range(5)]
new =[i for i in range(8) if i <= 3]
print(new)

address =["usilampatti","madurai","tamil nadu"]
detials =[x.upper() for x in address ]
print(detials)

# sort
slist =["app","game","version","animation"]
olist =[44,29.9, 1]
olist.sort()
slist.sort()
print(slist)
print(olist)

slist1 =["v","i","s","h","a","l","i","my name","apple"]
olist1 =[1,2,3,4,5,6,7,8]
slist1.sort(reverse=True)
olist1.sort(reverse=True)
print(slist1)
print(olist1)

# case insentivity
upcase =["small", "Customize" ,"Apple","food","call"]      #???????
upcase.sort()
#  upcase.reverse()
upcase.sort(key=str.lower)
print(upcase)   

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)

#copy of list
currentlist =["old list save for new list"]
newlist=currentlist.copy()
print(newlist)

oldlist =["copy of old list  "]
new = list(oldlist)
print(new)

adlist=[1,2,3,4]
anotherlist =[5,6,7,8]
mergelist =adlist +anotherlist
print(mergelist)

first =[10,20,30]
second =[40,50,60]
for x in second:
   first.append(x)
   print(first)

l =["a","b","c"]
m =[1,2,3,4]
l.extend(m)
print(l.count("a"))
print(l)
    
#  change =[1,2,3,4,5,6,7,8,9]
   
#  print(change[:5] and [6:] )                                





