
import calendar

print("specified the one month details")

year =int(input("enter the year:"))
month =int(input("enther the month:"))
#  date =int(input("enter the date:"))       # exctra space only showing 
print(calendar.month(year,month))            #,date))

print("**************")


print("all month printed using for loop")
no =12
yr =int(input("enter the year"))
for i in range(1 ,no) :
#for i in no :
    print(calendar.month(yr ,i))  

print("****************")  
print(calendar.calendar(yr))        #?????