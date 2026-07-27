
# Класс Calculator описывает калькулятор
class Calculator:
    # Атрибут класса: общий для всех объектов
    total_operations = 0

    def __init__(self, name):
        # Атрибуты экземпляра: принадлежат конкретному объекту
        self.name = name
        self.last_result = 0

    # Метод сложения
    def add(self, a, b):
        result = a + b
        self.last_result = result
        Calculator.total_operations += 1
        return result

    # Метод вычитания
    def subtract(self, a, b):
        result = a - b
        self.last_result = result
        Calculator.total_operations += 1
        return result

    # Метод умножения
    def multiply(self, a, b):
        result = a * b
        self.last_result = result
        Calculator.total_operations += 1
        return result

    # Метод деления
    def divide(self, a, b):
        if b == 0:
            return "Ошибка: деление на ноль"
        result = a / b
        self.last_result = result
        Calculator.total_operations += 1
        return result


# Создаем объект класса Calculator
calc = Calculator("Учебный калькулятор")

# Выводим имя калькулятора - атрибут экземпляра
print("Программа:", calc.name)

# Ввод чисел
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

# Меню
print("\nВыберите операцию:")
print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")

choice = input("Ваш выбор: ")

# Выполнение операции
if choice == "1":
    print("Результат:", calc.add(x, y))
elif choice == "2":
    print("Результат:", calc.subtract(x, y))
elif choice == "3":
    print("Результат:", calc.multiply(x, y))
elif choice == "4":
    print("Результат:", calc.divide(x, y))
else:
    print("Неверный выбор")

# Показ атрибутов
print("Последний результат:", calc.last_result)               # атрибут экземпляра
print("Всего операций:", Calculator.total_operations)         # атрибут класса

'''
'''

