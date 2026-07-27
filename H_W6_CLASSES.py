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


class User:
    country = "Israel"

    def __init__(self, username, age):
        self.username = username
        self.age = age


user1 = User("Anna", 22)
user2 = User("Dan", 29)
user3 = User("Mila", 31)

print(User.country)
print(user1.country)


User.country = "Canada"

print(User.country)
print(user1.country)

