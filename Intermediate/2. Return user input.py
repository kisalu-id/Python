from company import dlg
from sclcore import do_debug
from datetime import date

# as a basis we can use the previous script

#goal:
#program that asks the user:
#his name
#his birthday
#his hobbies
#how he would rate this program out of 10

#the program then answers the user with one output containing:
#Your Name is ...
#You are ... years old
#Your next birthday is in ... days
#your hobbies are 
#we appreciate your rating of ... out of 10

# prebuild functions to use
# dlg.outputbox(text_to_output)              --> outputs a textbox in easywood
# dlg.input_box(caption=, title=)            --> creates an inputbox in ew, returns the input as a string
# date.today()                               --> gives back current date
# string.split(seperator)                    --> google what it does

do_debug()
name = dlg.input_box(caption="What's your name?", title="Name?")
birthday = dlg.input_box(caption="bspw. 28.03.1995", title="Birthday?")   
hobbies_str = dlg.input_box(caption="What are your hobbies?", title="Hobbies?")
rating = dlg.input_box(caption="How do you rate this program?", title="Rate?")   
curr_date = str(date.today())


#dlg.output_box(f"Test 1 {curr_date}")
birhtday_list = birthday.split(".")
curr_date_list = (curr_date).split("-")
#dlg.output_box(f"Test 2 {curr_date_list}")

day_bd = int(birhtday_list[0])
month_bd = int(birhtday_list[1])
year_bd = int(birhtday_list[2])

year_t = int(curr_date_list[0])
month_t = int(curr_date_list[1])
day_t = int(curr_date_list[2])

age = year_t - year_bd

day_d = day_bd - day_t
month_d = month_bd - month_t

if month_d < 0:
    month_d += 12

if month_d == 0:
    if day_d < 0:
        day_d += 365

day_d += month_d * 30

dlg.output_box(f"Your name is {name}")
dlg.output_box(f"You are about {age} years old")
dlg.output_box(f"Your next birthday is in {day_d} days")
dlg.output_box(f"Your hobbies are {hobbies_str}")
dlg.output_box(f"We appreciate your rating of {rating} out of 10")
