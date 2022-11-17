# b5.2.5
# a = 0
# b = 0
#
# while id(a) == id(b):
#     a -= 1
#     b -= 1
# print(a, b)

# b5.2.9
# new_text = set(input('Enter your text: '))
# print('Amount of unique symbols: ', len(new_text))

# b5.2.12
a = input('enter numbers: ').split()
b = input('enter numbers: ').split()
set_a, set_b = set(a), set(b)
print(set_a)
print(set_b)
print(set_a.symmetric_difference(set_b))
