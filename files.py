# Open file.

f =open("E:\\VISHALI\\aaa.txt", "r")
print(f.read(5))

# Readline
f =open("E:\\VISHALI\\aaa.txt", "r")
print(f.readline())

# loop
f =open("E:\\VISHALI\\aaa.txt", "r")
for i in f:
    print(i)
f.close()    


f =open("E:\\VISHALI\\aaa.txt", "a")
f.write("vishali")
f.close()
f =open("E:\\VISHALI\\aaa.txt", "r")
print(f.read())

f = open("E:\\VISHALI\\aaa.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("E:\\VISHALI\\aaa.txt", "r")
print(f.read())


f =open("VISHALIN.txt","a") 
f.write(" i am fine.")
f.close()

import os
os.remove("VISHALIN.txt")



