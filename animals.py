# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         return '....'
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return 'Woff!'
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return 'Mau!'
#
#
# dog = Dog('BOB')
# cat = Cat('Abaa')
#
# print(dog.name, 'says', dog.make_sound())
# print(cat.name, 'says', cat.make_sound())
#
#
# class Fish(Animal):
#     pass
#
#
# fish = Fish('Nemo')
#
# print(fish.name, 'says', fish.make_sound())
#
#
# # --- Учебный пример: атрибуты класса и атрибуты экземпляра ---
#
# class AnimalInfo:
#     # Атрибут класса.
#     # Он общий для всех объектов этого класса.
#     kingdom = 'Animal'
#
#     def __init__(self, name, age):
#         # Атрибуты экземпляра.
#         # Они принадлежат конкретному объекту.
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print('Name:', self.name)
#         print('Age:', self.age)
#         print('Kingdom:', AnimalInfo.kingdom)
#
#
# # Создаем два разных объекта одного класса.
# info1 = AnimalInfo('Bob', 3)
# info2 = AnimalInfo('Murka', 5)
#
# print()
# print('--- Class and instance attributes ---')
# info1.show_info()
# print()
# info2.show_info()
#
#
# # --- Короткий пример по теме: классы, объекты, наследование, полиморфизм ---
#
# class Bird:
#     # Атрибут класса: общий признак для всех птиц.
#     kind = 'bird'
#
#     def __init__(self, name):
#         # Атрибут экземпляра: имя конкретной птицы.
#         self.name = name
#
#     def speak(self):
#         # Базовое поведение.
#         return 'some sound'
#
#
# class Parrot(Bird):
#     # Наследование: Parrot получает всё от Bird.
#     # Полиморфизм: метод speak() работает по-другому.
#     def speak(self):
#         return 'hello'
#
#
# class Sparrow(Bird):
#     def speak(self):
#         return 'chirp'
#
#
# parrot = Parrot('Kesha')
# sparrow = Sparrow('Chick')
#
# print()
# print('--- OOP example ---')
# print(parrot.name, parrot.kind, parrot.speak())
# print(sparrow.name, sparrow.kind, sparrow.speak())
#
#
# # --- assert и unittest ---
#
# # assert - это простая проверка условия.
# # Если условие False, программа сразу выдаст ошибку AssertionError.
#
# def add(a, b):
#     return a + b
#
#
# assert add(2, 3) == 5
#
#
# # unittest - это отдельный фреймворк для тестов.
# # Он удобен, когда тестов много и их нужно запускать системно.
#
# import Class01_calculator
# import unittest
#
# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(10, 5), 15)
#
#
# if __name__ == '__main__':
#     unittest.main()
