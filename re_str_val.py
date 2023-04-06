import re
x = "vishali is testing Code for viji codeing  this  vinoyu test is  abcnoabc for re"
y =re.split("\s", x)
for i in range(4):
   pattern = input("enter message : ")
   if pattern=='vi%':
      pattern=('^vi.*')
   elif pattern=='%ng':
      pattern=('.*ng$')
   elif pattern=='%no%':
      pattern=('^.*\Bno.*$')
   else :
       print('Invailed input string .')
       raise SystemExit()
   for xx in y:
      start_letter = re.findall(pattern,xx)
      if (start_letter):
         print(" letter is  : ",start_letter)
  