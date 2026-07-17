
def create_profile(name, age=18, city="Unknown"):
    return {
        "name": name,
        "age": age,
        "city": city,
    }

print(create_profile("Anna"))
print(create_profile("Tom", 25))
print(create_profile(city="Haifa", name="Nadja"))

# 2. Написать функцию
# sum_even_numbers(*numbers)
# Функция принимает любое количество чисел.
# Нужно вернуть сумму
# только чётных
# чисел.
# Если аргументы не переданы — вернуть 0.

def sum_even_nums(*args):
    total = 0

    for num in args:
        if num % 2 == 0:
            total = total + num

    return total

print(sum_even_nums(1, 2, 3, 4, 5, 6)) # 12
print(sum_even_nums(7, 9)) # 0
print(sum_even_nums()) # 0

def sum_odd_nums(*args): # создает *список* аргументов(любых значений)

    nums = [num for num in args if num % 2 !=0]
# объявляем неизвестную переменную в список - для каждого неизвестного номера прогоняем цикл
    return sum(nums)

print(sum_even_nums(1, 2, 3, 4, 5, 6)) # 12
print(sum_even_nums(3, 6, 8)) # 14
print(sum_even_nums()) # 0


def pet(name, **items):
    print(f"Name: {name}")  # сначала выводим имя питомца

    if items:  # если дополнительные параметры есть
        for key, value in items.items():  # берём каждую пару ключ-значение
            print(f"{key}: {value}")  # выводим её в нужном формате
    else:
        print("No additional information")  # если параметров нет


def pet(name, **items):
    print(f"Name: {name}")

    if items:
        for key in items:
            print(f"{key}: {items[key]}")
    else:
        print("No additional information")

pet("Lucky", age=4, color="White", breed="Spitz")
pet("Lucky")

def merge_lists(*lists):
    result = []

    for lst in lists:
        result.extend(lst)

    return result

def merge_lists(*lists):
    result = []

    for lst in lists:
        for item in lst:
            result.append(item)

    return result
print(merge_lists([1, 2], [3], [4, 5], []))
print(merge_lists())

