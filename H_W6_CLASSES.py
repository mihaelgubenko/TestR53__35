
#1---------------------------------------------------------
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"{self.name} works as {self.position} and earns {self.salary}"


emp1 = Employee("Anna", "QA Engineer", 7000)
emp2 = Employee("Dan", "Administrator", 7800)

print(emp1.get_info())
print(emp2.get_info())

#2----------------------------
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            return "Not enough products"


laptop = Product("Laptop", 1200, 5)

print(laptop.buy(2))
print("Remaining balance after purchase 2 pcs.:", laptop.quantity)
print(laptop.buy(10))
print("The balance has not changed:", laptop.quantity)

#3-------------------------
class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is riding"


car = Car()
bicycle = Bicycle()

print(car.move())
print(bicycle.move())

#4--------------------------
class User:
    country = "Israel"

    def __init__(self, username, age):
        self.username = username
        self.age = age


user1 = User("Anna", 22)
user2 = User("Dan", 29)
user3 = User("Mila", 31)

print(user1.country)
print(user2.country)
print(user3.country)

User.country = "Canada"

print(user1.country)
print(user2.country)
print(user3.country)
