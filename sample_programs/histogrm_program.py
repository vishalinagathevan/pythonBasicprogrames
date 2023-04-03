class Histogram_program:
 def __init__(self) -> None:
   pass
 def histogram ():
     no = int(input("Enter the number : "))
     ver=[int(i) for i in str(no)] 
     print(ver)
     for i in ver:
       print()
       for j in range(i):
         print("*",end= " ")
histo =Histogram_program         
histo.histogram()


                 