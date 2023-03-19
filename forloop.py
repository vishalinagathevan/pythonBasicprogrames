"""
num =[1,2,3,4,5]
for x in num:
    print(x)

# string
name = "vishali"
for i in name:
    print(i)   

for j in "pappa":
        print(j)    

# break statement
names =["anu","bava","charu","deva"]
for i in names:
     print(i)
     if i == "charu":
          break
     
for i in names:
     if i == "charu":
          break
     print(i)     

for i in names:
     if i == "charu":
          continue
     print(i) 

# rang function ()
for x in range(5):
     print(x, end =" ")
#?????

for x in range(5, 10):
     print(x)        

for k in range(1,6,2) :
     print(k) 
else:
     print("finished")   


#nested loop
bike =["royal enfiled","honda","pulsar"]
car =["bmw","suv","mpv","mvm"]         
for i in bike :
     for j in car:
          print(i ,j) 

for i in [1,2,3,4]:
     pass
    

ss ="codeing"
for x in ss:
     print(x)


q =["sky","moon","star"]
for x in q:
     print(x)

for x in range(5):
     print(x)     

# range      
for x in range(1 ,6,2):                        # range stap value cant be zero
     print(x)


ca ="name"
for  x in range (len(ca)):
     print(ca[x])

for x in range(10,200,40) :
     print(x)
       

for x in "friends":
     print(x,end=" * ")
     print("*********")


for i in range (2):
 for j in range(i):
         print(i,j) 
print()                 #???????????   


for i in range (2):
 for j in range(2):
         print(i,j) 
print()         

print("else block")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")                      #????????

"""
"""
for i in 4:
     print(i)
     for j in range (i):
          print(i,j) 
"""
print()
list1 =[0,1,2,3]
for i in range(4):
     print(i)
     for j in list1:
          print(i,j) 