#----------------------------------
#Exercise 1
# What is the correct keyword for defining functions in Python?
# def

#----------------------------------
#Exercise 2
# Create a function named my_function.
def my_function():
  print("Hello from a function")
# def my_function():

#----------------------------------
#Exercise 3
# Execute a function named my_function.
def my_function():
  print("Hello from a function")

my_function()
# my_function()


#----------------------------------
#Exercise 4
# Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
  print(fname)
# print(fname)

#----------------------------------
#Exercise 5
# Let the function return the x parameter + 5.
def my_function(x):
  return x + 5
# return x + 5


#----------------------------------
#Exercise 6
# If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
  print("The youngest child is " + kids[2])
# def my_function(*kids):

#----------------------------------
#Exercise 7
# If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
  print("His last name is " + kid["lname"])
# def my_function(**kid):

#----------------------------------