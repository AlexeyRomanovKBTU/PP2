###################################
# Python Sets
###################################

#----------------------------------
#Exercise 1
# Which one of these is a set?
# myset = {'apple', 'banana', 'cherry'}

#----------------------------------
#Exercise 2
# True or False.
# Set items cannot be removed after the set has been created.
# False

#----------------------------------
#Exercise 3
# True or False:
# A set cannot have two items with the same value.
# True

#----------------------------------
#Exercise 4
# Select the correct function for returning the number of items in a set:
fruits = {'apple', 'banana', 'cherry'}
print(len(fruits))
# print(len(fruits))

#----------------------------------


###################################
# Access Set Items
###################################

#----------------------------------
#Exercise 1
# True or False.
# You can access set items by referring to the index.
# False

#----------------------------------
#Exercise 2
# Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
# if "apple" in fruits:

#----------------------------------
#Exercise 3
# Consider the following code:
thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset)
# What will be the printed result?
# False

#----------------------------------

###################################
# Add Set Items
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for adding items to a set?
# add()

#----------------------------------
#Exercise 2
# Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
# fruits.add("orange")

#----------------------------------
#Exercise 3
# Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
# fruits.update(more_fruits)

#----------------------------------

###################################
# Remove Set Items
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for removing an item from a set?
# remove()

#----------------------------------
#Exercise 2
# Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
# fruits.remove("banana")

#----------------------------------
#Exercise 3
# Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
# fruits.discard("banana")

#----------------------------------
#Exercise 4
# Select the correct function to remove all items from a set:
fruits = {'apple', 'banana', 'cherry'}
fruits.clear()
# fruits.clear()

#----------------------------------

###################################
# Loop Sets
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for looping through the items of a set?
for x in {'apple', 'banana', 'cherry'}:
  print(x)
# for x in {'apple', 'banana', 'cherry'}:
#   print(x)

#----------------------------------
#Exercise 2
# Insert the missing part of the for loop below to loop through the items of a set.
myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)
# for x in myset:

#----------------------------------
#Exercise 3
# True or False. Sets are unordered, so when you loop through the items,
# the order will be totally random.
# True

#----------------------------------

###################################
# Join Sets
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for joining set1 and set2 into set3?
# set3 = set1.union(set2)

#----------------------------------
#Exercise 2
# What is a correct syntax for joining multiple sets into one new set called set5?
# set5 = set1 | set2 | set3 | set4

#----------------------------------
#Exercise 3
# There are many ways to join sets in Python.
# Which one of the following methods keeps ONLY the duplicates?
# intersection()

#----------------------------------