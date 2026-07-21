from pathlib import Path


# ТЕМА: try / except
# Простыми словами:
# try / except - это механизм обработки ошибки.
# Это НЕ песочница антивируса: код не изолируется от системы.
# Это скорее "аварийный план": если код сломался, программа знает, что делать.


# LOW LEVEL - низкий уровень.
# Эта функция только считает. Она не общается с пользователем и не печатает ошибки.
def calculate(a: float, b: float, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b  # Здесь может быть ZeroDivisionError, если b == 0
    else:
        raise ValueError("Unknown operation")  # Создаем свою ошибку, если операция неизвестна


# MIDDLE LEVEL - средний уровень.
# Эта функция превращает строки в числа.
def parse_and_calculate(a_str: str, b_str: str, op: str):
    a = float(a_str)  # Здесь может быть ValueError, если строка не является числом
    b = float(b_str)  # Здесь тоже может быть ValueError
    return calculate(a, b, op)


# HIGH LEVEL - высокий уровень.
# Здесь мы уже ловим ошибки и решаем, что показать человеку.
def safe_calculator(a_str: str, b_str: str, op: str):
    try:
        result = parse_and_calculate(a_str, b_str, op)  # Пробуем выполнить опасный участок кода
        print("Result:", result)  # Если ошибок нет, печатаем результат
    except ZeroDivisionError:
        print("Ошибка: нельзя делить на ноль")  # Обрабатываем деление на ноль
    except ValueError as error:
        print("Ошибка в данных:", error)  # Обрабатываем неправильное число или операцию


# Пример с файлом.
# Файл может отсутствовать, поэтому это тоже место возможного сбоя.
def read_user_file():
    try:
        with open("user.json", "r", encoding="utf-8") as nfile:
            print(nfile.read())
    except FileNotFoundError:
        print("Ошибка: файл user.json не найден")


# Пример создания файла, чтобы потом его можно было безопасно прочитать.
def create_user_file():
    user_file = Path("user.json")  # Создаем путь к файлу user.json

    with open(user_file, "w", encoding="utf-8") as nfile:
        nfile.write('{"name": "Maria", "age": 30}')


# TESTS / ПРИМЕРЫ

# Обычный успешный расчет
safe_calculator("10", "2", "/")

# Ошибка деления на ноль
safe_calculator("10", "0", "/")

# Ошибка: строку "hello" нельзя превратить в число
safe_calculator("hello", "2", "+")

# Ошибка: неизвестная операция
safe_calculator("10", "2", "%")

# Работа с файлом
create_user_file()
read_user_file()


# ДОПОЛНИТЕЛЬНЫЙ ПРИМЕР:
# Почему мы часто получаем строки, а потом превращаем их в числа.


age_from_input = "25"  # Представим, что пользователь ввел 25 через input(); input всегда возвращает строку
age_as_number = int(age_from_input)  # int() превращает строку "25" в целое число 25
print(age_as_number + 5)  # Теперь это число, поэтому можно прибавить 5


price_from_file = "19.99"  # Представим, что цена пришла из файла или CSV как строка
price_as_number = float(price_from_file)  # float() превращает строку "19.99" в дробное число 19.99
print(price_as_number * 2)  # Теперь с ценой можно делать математические действия


age_from_json = "30"  # Представим, что возраст пришел из JSON или API как строка
age_number = int(age_from_json)  # Превращаем строку "30" в число 30
print(age_number >= 18)  # Проверяем условие: возраст больше или равен 18


bad_number = "hello"  # Эта строка не похожа на число

try:
    number = float(bad_number)  # Пробуем превратить "hello" в число
    print(number)  # Эта строка выполнится только если преобразование получилось
except ValueError:
    print("Ошибка: строку нельзя превратить в число")  # Сюда попадем, если float() не смог сделать число


# ДОПОЛНИТЕЛЬНЫЙ ПРИМЕР:
# try / except / else / finally
# else выполняется только тогда, когда ошибки НЕ было.
# finally выполняется всегда: и если ошибка была, и если ошибки не было.


try:
    value = int("123")  # Пробуем превратить строку "123" в целое число
except ValueError:
    print("Это не число")  # Выполнится, если int() не сможет сделать число
else:
    print("Преобразование прошло успешно:", value)  # Выполнится только если ошибки не было
finally:
    print("Этот блок выполняется всегда")  # Выполнится в любом случае


try:
    value = int("gffgfg")  # Пробуем превратить строку "gffgfg" в число
except ValueError:
    print("Это не число")  # Выполнится, потому что "gffgfg" нельзя превратить в число
else:
    print("Преобразование прошло успешно:", value)  # Не выполнится, потому что была ошибка
finally:
    print("Этот блок выполняется всегда")  # Все равно выполнится, даже после ошибки
