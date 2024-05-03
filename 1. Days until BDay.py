from datetime import date
from company import dlg
from sclcore import do_debug

# how many days until i have birthday?
# a program that asks the user when his birthday is and tells him how many days until his next birthday
# for simplessness we will say each month has 30 days !

# output 1: how old is the person?
# output 2: how many days until his next birthday?

# prebuild functions to use
# dlg.outputbox(text_to_output)              --> outputs a textbox in easywood
# dlg.input_box(caption=, title=)            --> creates an inputbox in ew, returns the input as a string
# date.today()                               --> gives back current date
# string.split(seperator)                    --> google what it does


do_debug()

#get and typecast date of birthday 
bdayStr = dlg.input_box("When is your Birthday? Format: day month year", "Birthday")
dlg.output_box(bdayStr)
bdayList = (bdayStr).split(" ")

dayBD = int(bdayList[0])
monthBD = int(bdayList[1])
yearBD = int(bdayList[2])

#get and typecast today's date: 2024-05-02
todayStr = str(date.today())

#split a string into a list where each word is a list item:
todayList = (todayStr).split("-")
dlg.output_box(str(todayList)) #list 2024 05 02
#print(todayList)

yearT = int(todayList[0])
monthT = int(todayList[1])
dayT = int(todayList[2])

#main part
#take today's date and month, if theyre later than bday date and still in this current year
#count month difference, if negative than count back

#    BD  -  TD  
#  01.01 - 02.05 x    -1d 8mR   239  X
#  01.09 - 02.05 x    -1d 4m    119  X
#  09.01 - 02.05 x     7d 8mR   247  x
#  09.09 - 02.05 x     7d 4m    127  x

#  09.05 - 02.05 x     7d            x
#  01.05 - 02.05 x     364           x
#  02.05 - 02.05 x     0             x

dayD = dayBD - dayT

monthD = monthBD - monthT

if monthD < 0:
    monthD += 12

if monthD == 0:
    if dayD < 0:
        dayD += 365 # 01.05 - 02.05  - had BDay this month, before today. no else case bc of line 71

dayD += monthD * 30

dlg.output_box(f"You have Birthday in {dayD} days")




#A Class is like an object constructor, or a "blueprint" for creating objects.

#Methods in objects are functions that belong to the object.

#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belong to the class.

#class Person:
#def __init__(self, name, age):
#self.name = name
#self.age = age
#  p1.age = 55                   property
#  p1 = Person("John", 36)       p1 object
#  print(p1.name)
