# # b5.3.2
#
# some_var = (2,)
#
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# b5.3.3
# a = None # пустая строка
# b = a or 1
# print(b)

# b5.3.8
# a = 0
# b = 0
# if a and b:
#     print("Обе переменные истинные")
#     print(a, b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b)  # печать значения одной переменной, которая является истинной
# else:
#     print("Обе переменные ложные")
#     print(a, b)

# b5.3.9
# a = int(input())
# if a % 1 == 0:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(False)
#     else:
#         print(False)
# else:
#     print(False)

# b5.3.10
# a = int(input())
# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print(True)
# else:
#     print(False)

# a = int(input())
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print(True)
# else:
#     print(False)

# b5.3.11
# a = list(map(int, input('Enter numbers: ').split()))
# print(all(a))

# b5.3.12
# a = list(map(int, input('Enter numbers: ').split()))
# print(not any(a))

# b5.3.13
# multi_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
#
# for row in multi_table:
#     print(row)

# b5.3.14 and b5.3.15
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(L)
# print(any(L))

# b5.3.16
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(L)
# print(any(L) and not all(L))

# b5.3.17
# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10, 0, -1)]
# # 10 9 8 7 6 5 4 3 2 1
#
# N = [a * b for a, b in zip(L, M)]
# print(N)

# b5.3.18
new_text = 'aaabbccccdaa'
last = new_text[0]
count = 0
result = ''
for char in new_text:
    if char == last:
        count += 1
    else:
        result += last + str(count)
        last = char
        count = 1
result += last + str(count)
print(result)
