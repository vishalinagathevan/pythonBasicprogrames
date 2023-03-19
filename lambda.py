#A lambda function can take any number of arguments, but can only have one expression.
# lambda function express its must
x=lambda a : a+ 10
print(x(10))

print()

i =lambda x,y : x *y
print(i(10,4))

# lambda function
def lam_function(n):
    return lambda multiple : multiple * n
myfunction =lam_function(5)  
print(myfunction(10))      

def lam_function(n):
    return 2 * n
print(lam_function(6))


def lam_function(n):
    return lambda division : division / n
myfunction =lam_function(5) 
myfun =lam_function(2) 
print(myfunction(10))  
print(myfun(20)) 






