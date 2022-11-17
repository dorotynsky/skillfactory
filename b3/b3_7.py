# sum = 0 # заводим переменную счетчик, в которой мы будем считать сумму
# n = 5

# заводим цикл for в котором мы будем проходить по всем числам от одного до N
# for i in range(1, n + 1): # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print('sum in previous step: ', sum)
#     print('i in the moment: ', i)
#     sum += i # cуммируем текущее число i и перезаписываем значение суммы
#     print('sum after plus: ', sum)
#     print('---')
# print('end of the cycle')
# print()
# print('sum is: ', sum)

# b3.7.2
# p = 1
# n = 5
#
# for i in range(1, n + 1):
#     print('sum in previous step: ', p)
#     print('i in the moment: ', i)
#     p *= i
#     print('sum after plus: ', p)
#     print('---')
# print('end of the cycle')
# print()
# print('sum is: ', p)

n = 4
for i in range(1, n+1):
    print('*' * i)
