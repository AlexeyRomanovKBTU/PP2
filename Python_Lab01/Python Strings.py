###################################
# Python Strings
###################################

#----------------------------------
#Exercise 1
# What will be the result of the following code:
x = 'Welcome'
print(x[3])
# c

#----------------------------------
#Exercise 2
# Use the len function to print the length of the string.
x = "Hello World"
print(len(x))
# print(len(x))

#----------------------------------
#Exercise 3
# Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
# x = txt[0]

#----------------------------------
#Exercise 4
# Insert the correct keyword to check if the word 'free' is present in the text:

txt = 'The best things in life are free!'
if 'free' in txt:
  print('Yes, free is present in the text.')
# if 'free' in txt:

#----------------------------------


###################################
# Slicing Strings
###################################

#----------------------------------
#Exercise 1
# What will be the result of the following code:
x = 'Welcome'
print(x[3:5])
# co

#----------------------------------
#Exercise 2
# Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
# x = txt[2:5]

#----------------------------------
#Exercise 3
# What will be the result of the following code:
x = 'Welcome'
print(x[3:])
# come

#----------------------------------

###################################
# Modify Strings
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax to print a string in upper case letters?
# 'Welcome'.upper()

#----------------------------------
#Exercise 2
# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
# x = txt.strip()

#----------------------------------
#Exercise 3
# Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
# txt = txt.upper()

#----------------------------------
#Exercise 4
# Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
# txt = txt.lower()

#----------------------------------
#Exercise 5
# Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")
# txt = txt.replace("H", "J")

#----------------------------------

###################################
# String Concatenation
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax to merge variable x and y into variable z?
# z = x + y

#----------------------------------
#Exercise 2
# What will be the result of the following code:
x = 'Welcome'
y = 'Coders'
print(x + y)
# WelocomeCoders

#----------------------------------
#Exercise 3
# Consider this code:
a = 'Join'
b = 'the'
c = 'party'
# What is a correct syntax to print 'Join the party'?
# print(a + ' ' + b + ' ' + c)

#----------------------------------

###################################
# Format Strings
###################################

#----------------------------------
#Exercise 1
# If x = 9, what is a correct syntax to print 'The price is 9.00 dollars'?
# print(f'The price is {x:.2f} dollars')

#----------------------------------
#Exercise 2
# Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = f"My name is John, and I am {age}"
print(txt)
#txt = f"My name is John, and I am {age}"

#----------------------------------
#Exercise 3
# What will be the result of the following code:
print(f'The price is {2 + 3} dollars')
# The price is 5 dollars

#----------------------------------