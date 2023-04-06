#  Import regular expression .
import re
# Starting letter is only match.
some =input("Enter text : ")
text= some
start_letter = re.findall("^sh.*", text)
if (start_letter):
  print("Start letter is staring from sh : ",start_letter)
else:
  print("Start letter is not starting form sh: ",text)

#r1 =re.search("^\w+",xx)
#r1 = re.findall("^.*", xx)


# Start and end letter is same .
text =input("Enter text : ")
name =text
start_end =re.findall("^vi.*li$",name)
print("Start letter and end letter is same : ",start_end)

# Only end letter is same .
text1 =input("Enter text : ")
txt =text1
end_letter =re.findall(".*li$",txt)
print("Only end latter is same :",end_letter)



xxx="dwdwd wewew ewe wewe we"
y =re.split("\S", xxx)
print(len(y))
