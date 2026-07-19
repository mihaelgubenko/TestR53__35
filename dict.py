from urllib import response

books = {
    'Hary Potter': 'rowling',
    'To digg  the yard': 'Happer Lea'
}

books1 = {
    'Hary Potter',
    'To digg the yard'
}

print(books)
print(books1)

response = {
    'status': 'success',
    'user': {'id': 1, 'name': 'Mike'
             }}
print(response['user']['name'])
print('________________________________________________')
team_ages = {
    'Hary Potter': 15, 'Germiona': 16, 'Ron': 15.5}
print(team_ages.keys())
print('___________')
print(team_ages.values())

print('----------------')


#{'Germiona': 15, 'Ron': 16, 'Hary Potter': 15.5}
team_names = ['Germiona', 'Ron', 'Hary Potter']
team_ages = [15, 16, 15.5]

print(team_names)

team = {name: age for name, age in zip(team_names, team_ages)}
print(team)