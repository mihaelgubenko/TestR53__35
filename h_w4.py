import csv
import json
from pathlib import Path


def save_shopping_list(items):
    with open("shopping.txt", "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")


def read_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for student in reader:
            print(f"Student: {student['name']} ({student['age']})")


def save_profile(name, age, city):
    profile = {
        "name": name,
        "age": age,
        "city": city,
    }

    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4)


def create_reports_folder():
    reports_folder = Path("reports") / "homework" / "week_4"  # Создаем вложенный путь: reports/homework/week_4

    reports_folder.mkdir(parents=True, exist_ok=True)  # Создаем все папки по пути, если их еще нет

    result_file = reports_folder / "result.txt"  # Создаем путь к файлу result.txt внутри вложенной папки

    with open(result_file, "w", encoding="utf-8") as file:  # Открываем файл для записи в кодировке utf-8
        file.write("Homework completed successfully!")  # Записываем строку в файл


# Test 1: save a shopping list to shopping.txt
items = ["Milk", "Bread", "Apples", "Coffee"]
save_shopping_list(items)


# Test 2: create students.csv and read students from it
with open("students.csv", "w", encoding="utf-8", newline="") as file:
    file.write("name,age\n")
    file.write("Anna,21\n")
    file.write("Tom,19\n")
    file.write("Kate,22\n")

read_students("students.csv")


# Test 3: save a profile to profile.json
save_profile("Maria", 30, "Haifa")


# Test 4: create nested reports/homework/week_4 folder and result.txt inside it
create_reports_folder()

