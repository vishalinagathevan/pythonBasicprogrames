#Arrays are used to store multiple values in one single variable

animals =["cat","dog","dog"]
print(animals)

print("   Access the Elements of an Array  ")
num =[1,2,3,4,5,6,7]
x=num[2]
print(x)

num [1]="update the new value "
print(num)
print(len(num))

print("loop statement")
for i in num:
    print(i)

print("adding new value in array ")
num.append("vishali")    

# remove value 
num.pop(1)
print(num)            # remove 2 value

num.remove(3)
print(num)