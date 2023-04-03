#  Add a placeholder where you want to display the price
amount =849
product  ="Some pruduct {}"
#  Using string format() 
print(product.format(amount))

# A number with two decimals
price =455
variable=("The product price  is {:.3f} its fixed.")
print(variable.format(price))

#  Multiple Values
name_Of_studend ="first name is :{},Second name is{}"
print(name_Of_studend.format("vishali" ,"Tharanya"))

First_Rank ="kavin"
Last_Rank ="vino"
Rank = "Class 1st mark {} , The last rank is {}."
print(Rank.format(First_Rank,Last_Rank))

# Used to index value.
First_Rank ="kavin"
Last_Rank ="vino"
Rank = "Class 1st mark {1} , The last rank is {0}."
print(Rank.format(First_Rank,Last_Rank))

First_Rank ="kavin"
Last_Rank ="vino"
Rank = "Class 1st mark {1} , The last rank is {0}.{1} is a toper."
print(Rank.format(First_Rank,Last_Rank))


#  Named Indexes
citys ="{city} is a temple and famous in {flower} ."
print(citys.format(city= "Madurai",flower ="Jasmine flowers." ))

