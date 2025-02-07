# 1
class printContent:
    String1 = ""

    def __init__(self):
        self.String1 = ""

    def getString(self):
        res = input()
        return res

    def printString(self):
        print(self.getString().upper())
        return

obj = printContent()    
obj.printString()

# 2
class Shape:
    def __init__(self):
        self.area = 0

    def getArea(self):
        print("Area =", self.area)
    
class Square(Shape):
    def __init__(self, lentgh):
        super().__init__()
        self.area = lentgh * lentgh

x = Square(4)
x.getArea()

# 3
class Rectangle(Shape):
    def __init__(self, lentgh, width):
        super().__init__()
        self.area = lentgh * width

y = Rectangle(4, 2)
y.getArea()

# 4
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates of the point:", self.x, self.y)

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, point):
        print("Distance:", (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2))**0.5)
        
p1 = Point(0, 0)
p1.show()
p2 = Point(0, 0)
p2.move(8, 6)
p2.show()
p1.dist(p2)

# 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print("Deposit:", money)
        print("Balance:", self.balance)

    def withdraw(self, money):
        if self.balance > money:
            self.balance -= money
            print("Withdraw:", money)
            print("Balance:", self.balance)
        else:
            print("Cannot withdraw")

acc = Account("Alexey", 100.0)
acc.withdraw(200.0)
acc.deposit(150.0)
acc.withdraw(200.0)

# 6
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
number_list = list(filter(is_prime, numbers))
print("Prime numbers:", number_list)