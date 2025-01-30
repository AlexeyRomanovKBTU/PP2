###################################
# Python Tuples
###################################

#----------------------------------
#Exercise 1
# Which one of these is a tuple?
# thistuple = ('apple', 'banana', 'cherry')

#----------------------------------
#Exercise 2
# Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))
# print(len(fruits))

#----------------------------------
#Exercise 3
# True or False:
# Tuple items cannot be removed after the tuple has been created.
# True

#----------------------------------


###################################
# Access Tuple Items
###################################

#----------------------------------
#Exercise 1
# You can access tuple items by referring to the index number,
# but what is the index number of the first item?
# 0

#----------------------------------
#Exercise 2
# Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# print(fruits[0])

#----------------------------------
#Exercise 3
# Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
# print(fruits[-1])

#----------------------------------
#Exercise 4
# Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
# print(fruits[2:5])

#----------------------------------

###################################
# Update Tuples
###################################

#----------------------------------
#Exercise 1
# You cannot change the items of a tuple, but there are workarounds.
# Which of the following suggestion will work?
# Convert tuple into a list, change item, convert back into a tuple.

#----------------------------------
#Exercise 2
# Which is a correct syntax to delete a tuple?
# del mytuple

#----------------------------------
#Exercise 3
# True or False. You are allowed to add a tuple to an existing tuple.
# True

#----------------------------------

###################################
# Unpack Tuples
###################################

#----------------------------------
#Exercise 1
# Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
# banana

#----------------------------------
#Exercise 2
# Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
# What will be the value of y?
# ['banana', 'cherry']

#----------------------------------
#Exercise 3
# Consider the following code:
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
# What will be the value of y?
# ['banana', 'cherry']

#----------------------------------

###################################
# Loop Tuples
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for looping through the items of a tuple?
for x in ('apple', 'banana', 'cherry'):
  print(x)
# for x in ('apple', 'banana', 'cherry'):
#   print(x)

#----------------------------------
#Exercise 2
# Insert the missing part of the while loop below to loop through the items of a tuple.
mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1
# while i < len(mytuple):

#----------------------------------
#Exercise 3
# Insert the missing part of the for loop below to loop through the items of a tuple
# by using the range function to loop through the tuple's index numbers.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# for i in range(len(thistuple)):

#----------------------------------

###################################
# Join Tuples
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for joining tuple1 and tuple2 into tuple3?
# tuple3 = tuple1 + tuple2

#----------------------------------
#Exercise 2
# What is a legal way to turn this tuple: (1,2,3) into this tuple:(1,2,3,1,2,3)?
tuple1 = (1,2,3)
tuple1 = tuple1 * 2
# tuple1 = (1,2,3)
# tuple1 = tuple1 * 2

#----------------------------------
#Exercise 3
# Consider the following code:
tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1
# What will be the value of tuple3?
# (1, 2, 3, 'a', 'b', 'c')

#----------------------------------