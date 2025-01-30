###################################
# Python Lists
###################################

#----------------------------------
#Exercise 1
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])
# banana

#----------------------------------
#Exercise 2
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])
# banana

#----------------------------------
#Exercise 3
# True or False.
# List items cannot be removed after the list has been created.
# False

#----------------------------------
#Exercise 4
# Select the correct function for returning the number of items in a list:
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))
# len

#----------------------------------


###################################
# Access List Items
###################################

#----------------------------------
#Exercise 1
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])
# cherry

#----------------------------------
#Exercise 2
# Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# fruits[1]

#----------------------------------
#Exercise 3
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])
# ['banana', 'cherry', 'orange']

#----------------------------------
#Exercise 4
# Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
# 2:5

#----------------------------------

###################################
# Change List Items
###################################

#----------------------------------
#Exercise 1
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])
# banana

#----------------------------------
#Exercise 2
# Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
# fruits[0] = "kiwi"

#----------------------------------
#Exercise 3
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])
# mango

#----------------------------------

###################################
# Add List Items
###################################

#----------------------------------
#Exercise 1
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])
# apple

#----------------------------------
#Exercise 2
# Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
# fruits.append("orange")

#----------------------------------
#Exercise 3
# Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
# fruits.insert(1, "lemon")

#----------------------------------
#Exercise 4
# Select the missing parts to add the elements of tropical to fruits:
fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)
# fruits.extend(tropical)

#----------------------------------

###################################
# Remove List Items
###################################

#----------------------------------
#Exercise 1
# What is a List method for removing list items?
# pop()

#----------------------------------
#Exercise 2
# Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# fruits.remove("banana")

#----------------------------------
#Exercise 3
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)
# ['apple', 'cherry']

#----------------------------------
#Exercise 4
# Select the correct function to remove all items from a list:
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
# fruits.clear()

#----------------------------------

###################################
# Loop Lists
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for looping through the items of a list?

# for x in ['apple', 'banana', 'cherry']:
# print(x)

#----------------------------------
#Exercise 2
# Insert the missing part of the while loop below to loop through the items of a list.
mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1
# while i < len(mylist):

#----------------------------------
#Exercise 3
# What is a correct syntax for looping through the items of a list?

# [print(x) for x in ['apple', 'banana', 'cherry']]

#----------------------------------

###################################
# List Comprehension
###################################

#----------------------------------
#Exercise 1
# Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
# What will be the value of newlist?

# ['banana']

#----------------------------------
#Exercise 2
# Fill in the missing parts to complete the list comprehension:
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]
# newlist = [x for x in fruits]

#----------------------------------
#Exercise 3
# Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
# What will be the value of newlist?

# ['apple', 'apple', 'apple']

#----------------------------------

###################################
# Sort Lists
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for sorting a list?
# mylist.sort()

#----------------------------------
#Exercise 2
# What is a correct syntax for reversing the current order of a list?
# mylist.reverse()

#----------------------------------
#Exercise 3
# What is a correct syntax for sorting a list descending?
# mylist.sort(reverse = True)

#----------------------------------

###################################
# Copy Lists
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for making a copy of a list?
# list2 = list1.copy()

#----------------------------------
#Exercise 2
# What is a correct syntax for making a copy of a list?
# list2 = list(list1)

#----------------------------------
#Exercise 3
# What is a correct syntax for making a copy of a list?
# list2 = list1[:]

#----------------------------------

###################################
# Join Lists
###################################

#----------------------------------
#Exercise 1
# What is a correct syntax for joining list1 and list2 into list3?
# list3 = list1 + list2

#----------------------------------
#Exercise 2
# What is a correct syntax for adding elements from list2 into list1?
# list1.extend(list2)

#----------------------------------
#Exercise 3
# Consider the following code:
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
# What will be the value of list1?

# ['a', 'b', 'c', 1, 2, 3]

#----------------------------------