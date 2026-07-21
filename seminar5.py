with open("f1.txt", "r") as file:
    # content = file.read()
    # print(content)

    for l in file:
        print(l.strip())

import csv


# csv

student = [['name', 'age', 'city'],
    ['na1', 34, 'Haifa'],
    ['na2', 30, 'Karmiel'],
    ['na3', 40, 'Jerusalem']]
with open('students.csv', 'w', encoding='utf-8', newline='') as stud:
    w = csv.writer(stud)
    w.writerows(student)


with open('students.csv', 'r') as stud:
    pass

