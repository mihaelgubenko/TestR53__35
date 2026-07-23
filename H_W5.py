def get_list_element(items, index):
    try:
        return items[index]
    except IndexError:
        return "Index is out of range"



numbers = [10, 20, 30]
print(get_list_element(numbers, 1))
print(get_list_element(numbers, 10))

# 2
def get_user_data(user, key):
    try:
        return user[key]
    except KeyError:
        return "Key was not found"


user = {"name": "Anna", "age": 30}
print(get_user_data(user, "name"))
print(get_user_data(user, "email"))

#3
def calculate_average(first_value, second_value):
    try:
        num1 = float(first_value)
        num2 = float(second_value)
        return (num1 + num2) / 2
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"


print(calculate_average("10", "20"))
print(calculate_average("hello", "20"))
print(calculate_average(None, 20))

#4
def read_number():
    try:
        user_input = input("Enter a number: ")
        int(user_input)
        print("Number was entered successfully")
    except ValueError:
        print("Invalid number")
    finally:
        print("Program finished")

#5
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is not realistic")
