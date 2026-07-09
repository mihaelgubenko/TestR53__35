# s1 = 'strrr!'
# s2 = "sttrr2"
# text1 =  "I want to say: \"Good Bye\""
# print(text1)
#
#
# txt2 = 'I want to say: Good Bye'
# print(len(txt2))
# lon_string  = '12345 ' * 4
# print(lon_string)
# city = 'Jerusalem'
# temp = 28.5
# print('city')
# text = f'Today in {city} the temp is {temp + 3}' # aDD + 3
# print(text)
#
# print(text.upper()) # CAPS
# print(city[3]) # give me the 1st element in the word
# print(city[-1])
# num_string = '0123456789'
# print(num_string[2:])
# print(num_string[:2])
# print(num_string[2:len(num_string)])
# print(num_string[::-1]) # revers of string
from datetime import date

exmple = " I like walking "
# print(exmple.upper())
# print(exmple.lower())
# print("I like walking ".capitalize())
#
# print(exmple.strip())
# print(exmple.lstrip())
# print(exmple.rstrip())
print(exmple.strip().replace('walking ', 'hiking'))

text6 = 'I like walking' # разбитие на части
parts = text6.split(' ')
print(parts)
print(','.join(parts)) # сборка частей !

print(text6.find('walking')) # найти индекс слова
print(text6.count('walking')) # проверка на количество раз а
print('12345'.isdigit())
print('wert'.isalpha())

raw = ' Today is a good day '
print(raw.strip())
print(raw.replace(' ','*'))
date_str = '09-07-26'
print('Year: ' + date_str.split('-')[0], 'Month:' + date_str.split('-')[1], 'Day:' + date_str.split('-')[2])
