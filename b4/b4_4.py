# b4.4.1
# def fgen(start_position=3, step=2):
#     while True:
#         yield start_position
#         start_position += step
#
#
# a = fgen()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# b4.4.2
def repeat_list(lst):
    while True:
        for elem in lst:
            yield elem


for i in repeat_list([1, 2, 3]):
    print(i, end=' ')
