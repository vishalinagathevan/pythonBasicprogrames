#  Create an one variable 
#  Using in-build method 
lower_Case ="ProgrAm." 
# Create a for loop statement.
for i in lower_Case:
    if i .islower(): 
         print("Only lowerCase printer:",i)
print()         

Name ="VishaLI"
Lower_Case_Latters =[i for i in Name if i.islower() ]  
upper_Case_Latters =[i for i in Name if i.isupper() ]  
print("Lower_Case_Latter : ",Lower_Case_Latters) 
print("upper_Case_Latters : ",upper_Case_Latters) 