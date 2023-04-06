""""
import re
sentence = "vishali is testing Code for viji codeing  this  vinoyu test is  abcnoabc for re"
word =sentence.split()
count =0
for w in word:
    if re.match('^i.*',w):
        count += 1
print("Number of words starting with i : ",count )
"""
import re
sentence =input("Enter a sentance : ")
pattern = input("Enter a regular expression pattern: ")
words =sentence.split()
ans =[]
for w in words:
    if re.match(pattern,w):
     ans.append(w)   
print(" Words matching the pattern : ",ans)