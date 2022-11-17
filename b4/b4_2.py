# def char_frequency(text):
#     text = text.lower()
#     text = text.replace(' ', '')
#     text = text.replace('\n', '')
#
#     chars_list = {}
#     for char in text:
#         if char in chars_list:
#             chars_list[char] += 1
#         else:
#             chars_list[char] = 1
#
#     for item in chars_list.items():
#         print(item)
#
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """

# char_frequency(text)

# # b4.2.1
# def print_2_add_2():
#     print(2 + 2)
#
# print_2_add_2()
#
# # b4.2.2
# def print_hello_world():
#     print('Hello World')
#
# print_hello_world()

# def pow(base, n=2):
#     print(base ** n)
#
#
# pow(2, 3)

# b4.2.3
# def is_divider(dividend, divider):
#     if dividend % divider == 0:
#         print(f'{divider} is a divider of the dividend {dividend}')
#     else:
#         print(f'{divider} is NOT a divider of the dividend {dividend}')
#
#
# is_divider(10, 3)

# b4.2.4
# def ledder_of_stars(number):
#     # while number != 0:
#     #     print('*' * number)
#     #     number -= 1
#
#     for i in range(number, 0, -1):
#         print('*' * i)
#
#
# ledder_of_stars(3)

# b4.2.5
# def number_of_dividers(dividend):
#     count = 0
#     for i in range(dividend, 0, -1):
#         if dividend % i == 0:
#             count += 1
#     return count
#

# print(number_of_dividers(4))

# b4.2.6
def is_polindrome(text):
    text = text.replace(' ', '')
    text = text.lower()
    mirror_text = text[::-1]
    return text == mirror_text


print(is_polindrome('test'))
