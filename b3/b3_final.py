# Помните, в прошлом модуле мы с вами разбирали, как определить, содержит ли число цифры цифры, 5, 7 или 9:
#
# if ‘5’ in str(num):
#
# Напишите алгоритм, который делает то же самое, но работает только с числом, не приводя его в строку.
#

number_iter = -15878467
number_iter = abs(number_iter)

while True:
    number_check = number_iter % 10
    number_iter = number_iter // 10
    if number_check == 5:
        print(True)
        break
    elif number_iter <= 0:
        print(False)
        break
