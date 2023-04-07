# variable assign the nummeric value
# using in-build method in isnumeric 
str_value ="1244567"
print("The String Is Numeric :", str_value.isnumeric())
str1_value ="1AB44567"
print("The String Is Numeric :", str1_value.isnumeric())

# without using in-build method    ????
Str_NumericValue="12hhg345"
if Str_NumericValue.isnumeric:
    print("YES THIS IS NUMERIC VALUE ")
else:
    print("NO THIS IS NOT NUMERIC VALUE")    

