import re
x = "vishali is testing Code for viji codeing  this  vinoyu test is  abcnoabc for re"
y =re.split("\s", x)
#  pattern = input("enter message : ")
for xx in y:
      start_letter = re.findall("^[A-Za-z]*$",xx)
      if (start_letter):
         print(" letter is  : ",start_letter)