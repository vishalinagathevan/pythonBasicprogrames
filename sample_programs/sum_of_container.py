
# use inbuild method
t1=(10,20,30)
temp =sum(t1)
print(temp)

# using without inbuild method for tupel
x =(1,2,3,4)
a=0
for i in x:
  a=a+i
print(a)  

# with using in build method
marks =[50,70,90]
print(sum(marks))

# without using in build method in list
a=0
for i in marks:
  a=a+i
print(a)

# with using in build method in set
s ={50,10,20,50}   #cant sum duplicate values
print(sum(s))

#without using in build method in set
x=0
for i in s:
  x=x+i
 # print(x)   50,60,80
print(x) 

# with using in build method function
yy ={"a":10,"b":20,"c":20,}            #"a":11}
print(sum(yy.values()))

# without using in build method 
ver =0
for key, value in yy.items():
  ver =ver+value
print(ver)
