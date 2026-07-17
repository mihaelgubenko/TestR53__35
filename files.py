# with open('greeting.txt', 'w', encoding='utf-8') as file:
#     file.write('Hello world !')
#     file.write('\n')
#     file.write('Hello world add !')
#     file.write('\n')
#     file.write('Hello world wellness!')
#
# # r - read
# # w - write
# # a - append
# # r+ - read & write
# # rb, wb, - PDF, screenshots
#
# def log_test_result(test_name, stutus):
#
#     with open('run_test.log', 'w', encoding='utf-8') as  log_file:
#         log_file.write(f' {test_name}: {stutus} \n ')
#
#
# log_test_result('test_log', 'Passed')
# log_test_result('test_log', 'Failed')
# # log_test_result('test_reg', 'Passed')
# # log_test_result('test_logout', 'Failed')
#
# with open("data.txt", "w", encoding='utf - 8') as file:
#     file.write("This is some data\n"  "This is another data\n" "The next data")
#     with open("data.txt", "r", encoding='utf - 8') as file:
#         content = file.read()
#     print(content)
#     print(len(content))
#
# with open("data.txt", "r", encoding='utf - 8') as file:
#     lines = file.readlines()
# print(lines)
#
# for line in lines:
#     print(line.strip())
import csv

with open("users.csv", "w", encoding= 'utf - 8', newline= '') as user_file:
    writer = csv.writer(user_file)

    writer.writerow(["name", "email", 'role'])
    writer.writerow(['Anna', "ann@gmai.com", 'admin'])