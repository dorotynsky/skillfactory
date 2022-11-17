# b5.5.1
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))

# b5.5.2
# L = [-2, -1, 0, 1, -3, 2, -3]
#
#
# def even(x):
#     return x % 2 == 0
#
#
# print(list(filter(even, L)))

# b5.5.3
# (вес, рост)
# data = [
#     (82, 1.91),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84)
# ]
# sorted(data, key=lambda x: x[0] / x[1] ** 2)

# b5.5.4
# data = [
#     (82, 1.91),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84)
# ]
# min_index = sorted(data, key=lambda x: x[0] / x[1] ** 2)[0]
# print(min_index)
# print(min(data, key=lambda x: x[0] / x[1] ** 2))

# b5.5.5
a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))

# b5.5.6
a = ["это", "маленький", "текст", "обидно"]

print(list(map(str.upper, a)))
