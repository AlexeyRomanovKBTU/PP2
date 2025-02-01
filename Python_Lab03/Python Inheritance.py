#----------------------------------
#Exercise 1
# What is the correct keyword to use inside an empty class, to avoid getting an error?
# pass

#----------------------------------
#Exercise 2
# What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
# class Student(Person):

#----------------------------------
#Exercise 3
# We have used the Student class to create an object named x.
# What is the correct syntax to execute the printname method of the object x?
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
# x.printname()

#----------------------------------
