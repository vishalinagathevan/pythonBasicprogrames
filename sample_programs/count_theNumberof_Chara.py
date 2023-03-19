#count the number of occurrences of a specific character in a string.
print("COUNT THE NUMBERS OF CHARACTER IN STRING.")

# used to with count method  
print("used to in-build method function in count the string")
String_var =" hi...my name is vishali."
Temp=String_var.count("i")
print(Temp)

#used to without method
print("used to without in-build function in count the string.")
String ="count the number of charater in string. "
charter ="o"
count =0
for i in String:
    if i == charter:
        count += 1 
print(count)        