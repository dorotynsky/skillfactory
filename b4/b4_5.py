# import time
#
#
# def decorator_time(func):
#     def inner():
#         # print(f'начало функции {func}')
#         start_time = time.time()
#         func()
#         dif_time = time.time() - start_time
#         # print(f'конец функции {func}. Время выполнения: {dif_time}')
#         return dif_time
#
#     return inner
#
#
# @decorator_time
# def pow_2():
#     return 10000000 ** 2
#
#
# @decorator_time
# def in_build_pow():
#     return pow(10000000, 2)
#
#
# n = 100
# summe_pow_2 = 0
# summe_pow_in_build_pow = 0
# for n in range(n):
#     dif_time_pow_2 = pow_2()
#     summe_pow_2 += dif_time_pow_2
#     dif_time_in_build_pow = in_build_pow()
#     summe_pow_in_build_pow += dif_time_in_build_pow
#
# aw_pow_2 = summe_pow_2 / n
# aw_pow_in_build_pow = summe_pow_in_build_pow / n
# print(aw_pow_2)
# print(aw_pow_in_build_pow)

# b4.5.2
# def decorator(func):
#     count = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         func(*args, **kwargs)
#         count += 1
#         print(f'function {func} was called {count} times')
#     return wrapper
#
#
# @decorator
# def func_count():
#     print('Function works hard')
#
#
# func_count()
# func_count()
# func_count()

# b4.5.3
def decor_result_in_dict(func):
    result_dict = {}

    def wrapper(n):
        nonlocal result_dict
        if n not in result_dict:
            result_dict[n] = func(n)
            print(f'adding in the dict {result_dict[n]}')
        else:
            print(f'returning result from the dict {result_dict[n]}')
        print(f'result_dict lookl like: {result_dict}')
    return wrapper


@decor_result_in_dict
def f(n):
    return n * 123456789


f(1)
f(2)
f(3)
f(3)
