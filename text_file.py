import re
#  Create a new file. 
#  Used to open()--method.
file_read = open("PYTHON.txt","r")
file_write =open("PYTHON1.txt","w") 

save=file_read.read()
for i in save:
    if (i.isdigit() != True):
    #if i!= (re.findall("\D",save)):
        print(i,end=' ')
        file_write.write(i)
file_read.close()
file_write.close()

#Read a file and return the count of words in a text file.
filename ="PYTHON.txt"
numOfwords = 0
file= open(filename, 'r')
words = file.read().split()
for i in words:
  if (i.isalpha() ==True):
    numOfwords = numOfwords + 1
print("\n"+"Number of words :", numOfwords)
file.close()

fileopeing=open("PYTHON.txt","r")
count=0
lines=fileopeing.readlines()
for i in lines:
    count=count+1
    print(count,i)
fileopeing.close()

#  Read a file to List.
line=[]
open_file =open("PYTHON.txt","r")
for i in open_file:
   i = i.split("\s")
   line.append(i)
print("list of text : ",line)
open_file.close()   


#  Read a file into dictionary.

dictionary ={}
open_file1 =open("PYTHON.txt","r")
# X assing key values.
x=1
for i in open_file1:
   dictionary[x] = i
   x += 1        #??
print(" dictionary  : ",dictionary)
open_file1.close()   



     















