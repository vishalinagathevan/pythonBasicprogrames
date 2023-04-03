#  Import datetime modules
import datetime
#  Create a variable 
current_time =datetime.datetime.now()
# Diplay the year,month,date,hour,min,seconds,microseconds.
print(current_time)

# only Particular year,month and date.
particular_date =datetime.datetime(2001,1,7)
print("Particular year,month and date : ",particular_date)

#  Strformat time and date.
current_day = datetime.datetime(2023,3,28)
print("Small a is weekday sort version :",current_day.strftime("%a"))
print("Capital A is weekday full  version :",current_day.strftime("%A"))
print("Small b is month sort version :",current_day.strftime("%b"))
print("Capital b is month full  version :",current_day.strftime("%B"))
print("small c is Local version of date and time :",current_day.strftime("%c"))
print("Capital C is  show on current century : ",current_day.strftime("%C"))
print("Small d is day of month 1 to 31 : ",current_day.strftime("%d") )

current_day =datetime.datetime.now()
print("f microsecond : ",current_day.strftime("%f"))
