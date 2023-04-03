# Import regular expression 
import re
# Find the specified chratter.
txt = "The rain in Spain"
assign = re.findall("ai", txt)
print(assign)

text ="my name is vishali"
#Find all lower case characters alphabetically between "a" and "b":
store =re.findall("[a-b]",text)
print(store)

#Find all digit characters:
amount = "This product value is 1500 rs."
price =re.findall("[\d]",amount)
print(price )

# String start with(^) 
name = "kavi,vishali"
Name =re.findall("^v",name)
if Name:
    print("This name starts with v .")
else:
    print("V is not starts with name . ")    

name = "kavi,vishali"
Name =re.findall("i$",name)
if Name:
    print("This name ends with i .")
else:
    print("i is not ends with name . ")    


# Not match latters.
    name = "kavi,vishali"
Name =re.findall("tharanya",name)
print("Not match words :",Name)
if Name:
    print("This words is match .")
else:
    print("This words is not match ")    


#  Split
texts = "Madurai is temple city."
tem = re.split("\s", texts)
print(tem)

# Matacharacters
matachar ="Find all lower case characters alphabetically between "
lowerCase = re.findall("[a-b]",matachar)
print("Only show lowerCase latters ; ", lowerCase)

#Check if the string contains either "lower" or "upPer":
lowerCase1 = re.findall("lower|upper",matachar)
print("string contains either lower or uper anyone : ",lowerCase1 )
if lowerCase1:
    print("one words is match ")
else:
    print("Not match anyone")    


#  \ Special Sequences
# ( A ) start with particular words.
Student ="The students are best."
stu =re.findall("\AThe",Student)
if stu:
    print("Yes the steing starts with The . ")
else:
    print("This string not starts with The . ")    


    # ( b) ends with particular words.
Student ="The students are best."
stu =re.findall(r"The\b",Student)
if stu:
    print("Yes the steing starts with The . ")
else:
    print("This string not starts with The . ")   

#  "best" is present, but NOT at the beginning of a word(middle)
Student ="The best students are best."
stu =re.findall(r"\Best",Student)
print(stu)
if stu:
    print(" Yes This word is match  ")
else:
    print("No match . ")   

# w match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character) 
Student ="The best799_700 students are best."
stu =re.findall("\w",Student)
print(stu)
if stu:
    print(" match at every word character ")
else:
    print("No match . ")   

#(characters NOT between a and Z. Like "!", "?" white-space etc.):
Student ="The best7,99_700 ?stud.ents are> best!."
stu =re.findall("\W",Student)
print(stu)
if stu:
    print(" match at every word character ")
else:
    print("No match . ")   





