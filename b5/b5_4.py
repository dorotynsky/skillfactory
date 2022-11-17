# b5.4.1
# def linear_solve(a, b):
#     return b / a
#
#
# print(linear_solve(2, 9))
# # b5.4.2
# print(linear_solve(0,1))

# b5.4.3
# def discr(a, b, c):
#     return b ** 2 - 4 * a * c
#
#
# # b5.4.4
# def quadratic_solve(a, b, c):
#     if discr(a, b, c) < 0:
#         return 'Нет вещественных корней'
#     elif discr(a, b, c) == 0:
#         return -b / (2 * a)
#     else:
#         return (-b - discr(a, b, c) ** 0.5) / (2 * a), (-b + discr(a, b, c) ** 0.5) / (2 * a)

# b5.4.9
# def min_rec(new_list):
#     if len(new_list) == 1:
#         return new_list[0]
#     return new_list[0] if new_list[0] < min_rec(new_list[1:]) else min_rec(new_list[1:])
#
#
# print(min_rec([5, 2, 3, 6]))

# b5.4.10
# def mirror_rec(number):
#     if len(number) == 1:
#         return number
#     return number[-1] + mirror_rec(number[0:-1])
#
#
# print(mirror_rec(str(123456)))


# b5.4.11
# def equal(number, s):
#     if s < 0:
#         return False
#     if number < 10:
#         return number == s
#     return equal(number // 10, s - number % 10)
#
#
# print(equal(123, 6))

# b5.4.15
USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")


def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper


def has_access(func):
    def wrapper():
        if username in USERS:
            print("Юзернейм найден")
            func()
        else:
            print('Юзернейм не найден. Функция выполнена не будет')
    return wrapper


@is_auth
@has_access
def from_db():
    print("some data from database")


from_db()
