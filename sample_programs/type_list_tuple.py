#  Create a List and Tuple ,


List_Items =["apple","orange","mango"]
Tuple_Item =("cat","dog")
Set_Item={2,3,4,True,1}
print(" type ")
print(type(List_Items))
print(type(Tuple_Item))
print(type(Set_Item))


#  Using to if elif and else statement
#  Create a list
Type_of_collection =[1,2,3]
Type_of_collection1 =(1,2,3)
Type_of_collection2 ={1,2,3}
if type(Type_of_collection) == list:
    print ('a list')
if type(Type_of_collection1) == tuple:
    print ('a tuple')
if type(Type_of_collection2) == set:
    print ('a set')
else:
    print ('neither a tuple or a list')    

