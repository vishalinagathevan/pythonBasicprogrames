# unorder and unchngeable, unindexed, not allow duplicate
s_value ={"morning","afternoon","evening","midnight","earlymorning"}
print(s_value)

t_value ={"day","night"," day","night"}        # duplicte value dont allow (space is diffrence )
print(t_value)

same ={ True, 1,"vishali","age",18,False}        # 1 and true value is consider same in set .
print(same)                                         # 1 is cant consider length
print(len(same))

# set datatype 
set1={"vishali","sugrna","janani"}
set2 ={1,20,22.5,555,77777}
set3={True,False}
print(type(set1))
print(set2)
print(set3)

# constractor 
aset = set(("my name "," my age ","my name "))
print(aset)
print(type(aset))

# access
ss ={"apple","banana","pineapple","ornge",11,2,456,67.90}
for i in ss:
    print(ss,[i])

print("apple" in ss)
#  add 
ss.add("mango")
print(ss)

aaa ={"papaya","cherry","lemon"}
ss.update(aaa)
print(ss)

lii =["add list into tuple ","update"]
aaa.update(lii)
print(aaa)

# remove 
this = {"apple", "banana", "cherry","mango"}
this.remove("cherry")
this.discard("mango")
print(this)

tt ={"apple", "banana", "cherry","mango"}                 # rondom  value deleted
tt.pop()
print(tt)

ii ={"apple", "banana", "cherry","mango"}   
ii.clear()       # .del --- delete the set
print(ii)

# loop uisng 
zz ={"apple", "banana", "cherry","mango"}
for v in zz:
    print(v)    # len ??????   

#join
jj ={1,2,3,4,5}
kk ={5,6,7,4,2}
store =jj.union(kk)          # merge two set  cant merge duplicate
print(store)

a1set = {"a", "b" , "c"}
a2set = {1, 2, 3}
a1set.update(a2set)
print(a1set)

# only duplicate allows
set ={"apple", "banana", "cherry","mango"}
set1={"apple", "pineapple", "cherry","orange"}
set.intersection_update(set1)
set.intersection(set1)             #common words only take
print(set)

# NOT the Duplicates  only diffrence datas printed
idem ={"apple", "banana", "cherry","mango"}
idem1={"apple", "pineapple", "cherry","orange"}
idem.symmetric_difference_update(idem1)
idem.symmetric_difference(idem1)
save=idem.symmetric_difference(idem1)
print(idem)
print(idem)
print(idem)
print(save)






