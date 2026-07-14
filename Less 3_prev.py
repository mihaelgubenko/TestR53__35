def dobavit_rezultat_testa(nazvanie_testa, spisok_rezultatov=None):
    # Если список не передали, создаем новый
    if spisok_rezultatov is None:
        spisok_rezultatov = []
    spisok_rezultatov.append(nazvanie_testa)
    return spisok_rezultatov


# Функция добавляет название теста в список
print(dobavit_rezultat_testa("test_login"))
print(dobavit_rezultat_testa("test_logout"))


# Обычная функция
def uvoit(chislo):
    return chislo * 2


# Короткая анонимная функция
udvoit_lambda = lambda chislo: chislo * 2


# Обе строки выводят 20
print(uvoit(10))
print(udvoit_lambda(10))


spisok_chisel = [1, 2, 3]
# Умножаем каждый элемент списка на 2
rezultat_map = list(map(lambda chislo: chislo * 2, spisok_chisel))
print(rezultat_map)


spisok_chisel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Оставляем только четные числа
chetniye_chisla = list(filter(lambda chislo: chislo % 2 == 0, spisok_chisel))
print(chetniye_chisla)


# *args - принимает любое количество позиционных аргументов
def summa_chisel(*chisla):
    print(type(chisla), chisla)
    return sum(chisla)


print(summa_chisel(1, 2, 3))
print(summa_chisel(10, 20))
print(summa_chisel(10, 20, 40, 80, 90))
print(summa_chisel())


# *args удобно, когда нужно передать много чисел в одну функцию
def vyvesti_ocenki(student, *ocenki):
    print(f"Student: {student}")
    print("Scores:", ocenki)


vyvesti_ocenki("Anna", 90, 85, 100)
vyvesti_ocenki("Bob", 75)


# **kwargs - принимает любое количество именованных аргументов
def vyvesti_nastrojki(**nastrojki):
    print(type(nastrojki), nastrojki)
    return nastrojki


print(vyvesti_nastrojki(browser="chrome", headless=True, timeout=30))
print(vyvesti_nastrojki())


# **kwargs удобно, когда аргументы передаются как имя=значение
def sozdat_polzovatelya(**dannye):
    return dannye


polzovatel = sozdat_polzovatelya(name="Anna", role="admin")
print(polzovatel)
