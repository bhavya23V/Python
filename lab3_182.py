# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 11:19:29 2025

@author: Bhavya
"""

str1 = "ICT Department"
print(str1)

str1 = 'ICT Department'
print(str1)

str2 = "3EK2"
print(str2[1]) 

str3 = "ICT Department"
print(str3[-6])

str4 = "ICT Department"
print(str4[0:4])                              #till n-1 index

str4 = "ICT Department"
print(str4[:1]) 
print(str4[1:]) 

message = "ICT Department"
message[0] = "H"

message = "Bhavya V" 
message = "Bhavya "           #this will be printed
print(message)

msg = '''
Bhavya
ICT
3EK2
'''

print(msg)


str1 = 'Bhavya'
str2 = 'ICT'
str3 = '3EK2'

print(str1==str2)
print(str1==str3)

name = 'Bhavya '
sur_name = 'Vemula'
full_name = name + sur_name
print(full_name)

name = "Bhavya"
name = 'Bhavya'
print(len(name))

print("a" in 'aict')
print('a' not in 'ict')

message = "Bhavya"
print(message.upper())

message = "ICT_3EK2"
print(message.lower())

txt = "havya"
replaced = txt.replace('havya','Bhavya')
print(replaced)

message = "Python is fun"
print(message.find("q"))

message = "Python is fun"
print(message.index("q"))

title = "ICT DEPARTMENT     "
result = title.rstrip()
print(result)

txt = "Learning is fun"
print(txt.split())

message = "Python is fun"
print(message.startswith('is'))

no = '182'
print(no.isnumeric())

pin = "182"
# checks if every character of pin is numeric 
print(pin.isnumeric())


message = "Python is fun"
print(message.index('Python'))

name = 'Bhavya'
country = 'India'
print(f'{name} is from {country}')

str = "This is a \n normal string "
print(str)
raw_str = r"This is a \n raw string"
print(raw_str)


#post lab

