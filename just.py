import re
file_read = open("PYTHON.txt","r")
file_write =open("ALA.txt","w") 


lines=file_read.readlines()
regex ='^[0-9]+$' 

for i in lines:
    if re.search(regex,i):
        pass
    else:
        print(i,end=' ')
        file_write.write(i)
file_read.close()
file_write.close()    
