def function(x):
    if x.startswith("Is"):
      return x
    else:
     return "Is "+x
temp=input("enter any string:")
print(function(temp))
