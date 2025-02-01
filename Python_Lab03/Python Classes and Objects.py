#----------------------------------
#Exercise 1
# When the class object is represented as a string, there is a function that controls what should be returned, which one?
# __str__()

#----------------------------------
#Exercise 2
# What is a correct syntax for deleting an object named person in Python?
# del person

#----------------------------------
#Exercise 3
# Create a class named MyClass:
class MyClass:
  x = 5
# class MyClass:


#----------------------------------
#Exercise 4
# Create an object of MyClass called p1:
class MyClass:
  x = 5

p1 = MyClass()
# p1 = MyClass()

#----------------------------------
#Exercise 5
# Use the p1 object to print the value of x:
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)
# print(p1.x)

#----------------------------------
#Exercise 6
# What is the correct syntax to assign a "init" function to a class?
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
# def __init__(self, name, age):

#----------------------------------
#Exercise 7
# Insert the missing parts to make the code return: John(36):
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person('John', 36)
print(p1)
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person('John', 36)
print(p1)
"""

#----------------------------------