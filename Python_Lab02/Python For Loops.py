#----------------------------------
#Exercise 1
# What will be the result of the following code:
for x in range(3):
  print(x)
"""
0
1
2
"""

#----------------------------------
#Exercise 2
# Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# for x in fruits:

#----------------------------------
#Exercise 3
# In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":   
    continue
  print(x)
# continue

#----------------------------------
#Exercise 4
# Use the range function to loop through a code set 6 times.
for x in range(6):
  print(x)
# for x in range(6):

#----------------------------------
#Exercise 5
# Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    break
  print(x)
# break

#----------------------------------