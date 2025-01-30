###################################
# Python Dictionaries
###################################

#----------------------------------
#Exercise 1
# Which one of these is a dictionary?
# x = {'type' : 'fruit', 'name' : 'banana'}

#----------------------------------
#Exercise 2
# True or False.
# Dictionary items cannot be removed after the dictionary has been created.
# False

#----------------------------------
#Exercise 3
# True or False:
# A dictionary cannot have two keys with the same name.
# True

#----------------------------------
#Exercise 4
# Select the correct function to print the number of key/value pairs in the dictionary:
x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))
# print(len(x))

#----------------------------------


###################################
# Access Dictionary Items
###################################

#----------------------------------
#Exercise 1
# True or False.
# You can access item values by referring to the key name.
# True

#----------------------------------
#Exercise 2
# Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
# print(car.get("model"))

#----------------------------------
#Exercise 3
# Consider the following code:
x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])
# What will be the printed result?
# fruit

#----------------------------------

###################################
# Change Dictionary Items
###################################

#----------------------------------
#Exercise 1
# Consider the following code:
x = {'type' : 'fruit', 'name' : 'banana'}
# What is a correct syntax for changing the type from fruit to berry?
# x['type'] = 'berry'

#----------------------------------
#Exercise 2
# Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
# car["year"] = 2020

#----------------------------------
#Exercise 3
# Consider the following code:
x = {'type' : 'fruit', 'name' : 'banana'}
# What is a correct syntax for changing the name from banana to apple?
# x.update({'name': 'apple'})

#----------------------------------

###################################
# Add Dictionary Items
###################################

#----------------------------------
#Exercise 1
# Which one of these dictionary methods can be used to add items to a dictionary?
# update()

#----------------------------------
#Exercise 2
# Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
# car["color"] = "red"

#----------------------------------
#Exercise 3
# Insert the missing part to add an item to the dictionary.
x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color' : 'green'})
# x.update({'color' : 'green'})

#----------------------------------

###################################
# Remove Dictionary Items
###################################

#----------------------------------
#Exercise 1
# What is a dictionary method for removing an item from a dictionary?
# pop()

#----------------------------------
#Exercise 2
# Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
# car.pop("model")

#----------------------------------
#Exercise 3
# Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
# car.clear()

#----------------------------------
#Exercise 4
# Insert a correct syntax for removing the 'color' item of the dictionary:
myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar['color']
# del myvar['color']

#----------------------------------

###################################
# Loop Dictionaries
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for looping through the values of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
# for y in x.values():
#   print(y)

#----------------------------------
#Exercise 2
# What is a correct syntax for looping through the keys AND values of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
# for y, z in x.items():
#   print(y, z)

#----------------------------------
#Exercise 3
# Insert the missing part of the for loop below to loop through the items of a set.
myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)
# for x in myset:

#----------------------------------
#Exercise 4
# What is a correct syntax for looping through the keys of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
# for y in x.keys():
#   print(y)

#----------------------------------

###################################
# Copy Dictionaries
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for making a copy of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
# y = x.copy()

#----------------------------------
#Exercise 2
# One of these codes is NOT a correct way of making a copy of
# a dictionary named x, which one:
# y = x.duplicate()

#----------------------------------
#Exercise 3
# True or False. 
# Copied dictionaries will not be able to change its item values.
# False

#----------------------------------

###################################
# Nested Dictionaries
###################################

#----------------------------------
#Exercise 1
# Consider this syntax:
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
# what will be a correct syntax for printing the name 'May'?
# print(customers['c2']['name']

#----------------------------------
#Exercise 2
# Insert the missing part to loop through the keys and values of all nested dictionaries:
a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])
#for x, obj in customers.items():

#----------------------------------
#Exercise 3
# True or False. 
# A dictionary can only have one level of nested dictionaries.
# False

#----------------------------------