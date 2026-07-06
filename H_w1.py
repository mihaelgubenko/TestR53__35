# 1
s = input('')
if s == 'Shalom':
    print(s[::-1])
else:
    print('Wrong string')
phone = input('Enter phone number ')

# 2

if phone == '0' and len(phone) == 10 and phone.isdigit():
    print('TRUE')
else:
    print('FALSE')

# 3
s = input('Enter string: ')
start = int(input('Enter start: '))
finish = int(input('Enter finish: '))

if s is None or s.strip() == '':
    print('Wrong args')
elif start < 0 or finish >= len(s) or start > finish:
    print('Wrong args')
else:
    print(s[:start] + s[start:finish + 1][::-1] + s[finish + 1:])
