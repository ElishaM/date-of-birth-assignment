# date-of-birth-assignment
# this program asks for your name, year of birth, month of birth, date of birth and prints them together with the exact day of birth

import datetime

name=input('Whats your name: ')
y=int(input('Input the year of birth: '))
m= int(input('Input the month of birth(1-12): '))
d= int(input('Input the date of birth(1-31): '))
months = [
 'January',
 'February',
 'March', 
 'April',
 'May',
 'June',
 'July',
 'August',
 'September',
 'October',
 'November',
 'December' ]
 
 
month_name = months[m-1]

p = datetime.date(y,m,d)

print ( name, 'was born on', p.strftime('%a'),'/',d,'/',month_name,'/',y)
