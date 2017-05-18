
#date of birth


import calendar


age = int(input("Age: "))
date = int(input("Date Of Birth: "))
month_number = int(input("Month Of Birth: "))
current_year = int(input("Current year: "))
months =['January','February','March','April','May','June','July','August','September','October','November','December']
month_name =months[month_number -1]
year_of_birth = current_year - age

day_of_birth = calendar.weekday(year_of_birth, month_number, date)
day_string = calendar.day_name[day_of_birth]

print("You were born on " + day_string +"," + month_name +" in " + str(year_of_birth))
