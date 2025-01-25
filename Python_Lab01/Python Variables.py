###################################
# Python Variables
###################################

#----------------------------------
#Exercise 1
# What is a correct way to declare a Python variable?
# x = 5

#----------------------------------
#Exercise 2
# True or False:
# You can declare string variables with single or double quotes.
x = "John"
# is the same as
x = 'John'
# True

#----------------------------------
#Exercise 3
# True or False:
# Variable names are not case-sensitive.
a = 5
# is the same as
A = 5
# False

#----------------------------------
#Exercise 4
# Select the correct functions to print the data type of a variable:
# print(type(myvar))

#----------------------------------


###################################
# Variable Names
###################################

#----------------------------------
#Exercise 1
# Which is NOT a legal variable name?
# my-var = 20

#----------------------------------
#Exercise 2
# Create a variable named carname and assign the value Volvo to it.
# carname = "Volvo"

#----------------------------------
#Exercise 3
# Create a variable named x and assign the value 50 to it.
# x = 50

#----------------------------------

###################################
# Assign Multiple Values
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax to add the value 'Hello World', to 3 variables in one statement?
# x = y = z = 'Hello World'

#----------------------------------
#Exercise 2
# Insert the correct syntax to assign values to multiple variables in one line:
# x, y, z = "Orange", "Banana", "Cherry"

#----------------------------------
#Exercise 3
# Consider the following code:
fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)
#What will be the result of a
# apple

#----------------------------------

###################################
# Output Variables
###################################

#----------------------------------
#Exercise 1
# Consider the following code:
print('Hello', 'World')
# What will be the printed result?
# Hello World

#----------------------------------
#Exercise 2
# Consider the following code:
a = 'Hello'
b = 'World'
print(a + b)
# What will be the printed result?
# HelloWorld

#----------------------------------
#Exercise 3
# Consider the following code:
a = 4
b = 5
print(a + b)
# What will be the printed result?
# 9

#----------------------------------

###################################
# Global Variables
###################################

#----------------------------------
#Exercise 1
# Consider the following code:
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
# What will be the printed result?
# Python is awesome

#----------------------------------
#Exercise 2
# Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
  global x
  x = "fantastic"
# global x

#----------------------------------
#Exercise 3
# Consider the following code:
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
# What will be the printed result?
# Python is fantastic

#----------------------------------