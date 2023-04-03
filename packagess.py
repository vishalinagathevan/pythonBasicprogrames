# Import camalcase packege
import camelcase as cc
words =cc.CamelCase()
print(dir(cc))
# Some normal text covert to camelcase.
text ="Starting first latter is alway capital. this is camelcase change."
# Print the variable . use hump method.
print("CamelCase Example : ",words.hump(text))

