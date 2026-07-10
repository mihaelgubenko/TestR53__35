

numbers = (1, 2, 2342, 4,555, 6, 7, 5543, 9, 10)
t = tuple(sorted(numbers))
print(sorted(numbers, reverse=True))
print(min(numbers))
print(t)
# sorted - always new tuple or list
suntuple = numbers[3:7]
print(suntuple)

my_tuple = list(numbers)
print(my_tuple)

str = ''.join(map(str, numbers))
print(str)
print('-----------------------------------------')
# так видно как менять листы , неизменяемые , потом обратно.
my_tuple = (1,2,3,4,5) # НЕ ИЗМЕНЯЕМЫЙ
my_list = list(my_tuple) # ТЕПЕРЬ ИЗМЕНЯЕМЫЙ list
my_list[2] = 10 # ИЗМЕНИЛИ
updated_tuple = tuple(my_list) # СНОВА ПЕРЕВЕРНУЛИ В НЕ ИЗМЕНЯЕМЫЙ tuple
print("Original tuple: ", my_tuple)
print("Updated tuple: ", updated_tuple)


