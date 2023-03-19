# string  space can be  count 
name ="hi welcome"
print(name[2])

string_name="i'm vishali "
for i in string_name:
  print(i)  #,end= " ",)
  print( len(string_name))

 # check string 
txt ="This is my python practice programing"
print("practice" in txt)   # boolean

mes ="w3 schools is my learning platform"
if "sc1" in mes:
  print("yes!")
else:
  print("no...")  

txt1 ="This is my python practice programing"
print("practicess" not in txt1)

txt ="This is my python practice programing"
if "ok"not in txt:
  print("no this word")
else:
  print("yes this word is posible ")  


print("practice" in txt and "ok" not in txt)
print("practicess" in txt or "is" not in txt)

#slice string range start index 0  end index 5-1 
my ="how are you"
print(my[:8])  #starting index
print(my[1:5]) #particuler idexces
print(my[6:])  #end index

#nagatve slice  index start and end is nagative operater
pri ="slice the nagative number"  # nagative
print(pri[-15:],pri [:-15],pri[-11:-1])

#split ()only split the empty space (", Or * or any char ,")
ab ="i am studing in msc. It".split("s")
print(ab)

#concatnate
aa="wounder "
bb=" ful"
cc=aa+" "+bb
print(cc)

#format order must importab
no =15
game_name="foodball"
game_name2="runing"

st = "{0}the number of students and play the game in {2} and {1}"
print(st.format(no,game_name,game_name2))

#Escape Characters
sq ='i\'m fine'
print(sq)

rs='100\\'   #  hwo to use \\ in integer 
print(rs) 

nline=" this comment is \n nextline "    #\n \r (carriage returen) same ah??????
print(nline)








