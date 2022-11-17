import sys

# number = 1234567
# print('5' in str(number))

# N = 2234567
# N_string = str(N)
# print(int(N_string[0]) % 2 == 0)

# cost = int(input("Enter cost of sneakers"))
# if cost <= 2500:
#     print('Вы можете купить эти кроссовки!')
# else:
#     print('Увы, кроссовки слишком дорогие!')

# one = 12
# two = 13
#
# result = True if one < two else False
# print(result)

# hour = 5
# print("It's morning right now!") if 6 <= hour < 12 else print("It's not a morning")

# month_number = int(input('Enter month number: '))
# if month_number in [1, 2, 12]:
#     print('winter')
# elif month_number in [3, 4, 5]:
#     print('spring')
# elif month_number in [6, 7, 8]:
#     print('summer')
# elif month_number in [9, 10, 11]:
#     print('fall')
# else:
#     print('incorrect number')

# B3.4.3
# speed = int(input('Enter wind speed: '))
# if speed <= 0:
#     print('Error')
# elif 1 <= speed <= 4:
#     print('weak')
# elif 5 <= speed <= 10:
#     print('moderate')
# elif 11 <= speed <= 18:
#     print('strong')
# else:
#     print('hurricane')

# B3.4.4
# a = 77
# b = 177
# c = 177
# if a < 45 and b >=45 and c >= 45:
#     print(True)
# elif b < 45 and a >= 45 and c >= 45:
#     print(True)
# elif c < 45 and a >= 45 and b >= 45:
#     print(True)
# else:
#     print(False)

# B3.4.5
# a = 16
# if -10 <= a <= -1 or 2 <= a <= 15:
#     print(False)
# else:
#     print(True)

# good variant
# (number < -10 or number > -1) and (number < 2 or number > 15)

# B3.4.6
# number = 12344321
# number_mirror = int(str(number)[::-1])
# if number == number_mirror:
#     print('Number is a palindrom')
# else:
#     print('Number is NOT a palindrom')

# Result Exam
temperature = 25
isRain = False
isHeavyRain = False
clothes = ''

if temperature >= 30:
    print("Don't leave home")
    sys.exit()
elif 20 < temperature < 30:
    if isRain:
        clothes = 't-short, shorts and raincoat'
    else:
        clothes = 't-short and shorts'
elif 0 < temperature <= 20:
    if isRain:
        if isHeavyRain:
            clothes = 'coat, gummy boats and umbrella'
        else:
            clothes = 'coat and raincoat'
    else:
        clothes = 'coat'
else:
    clothes = 'Puhovik'
print('You have to wear: ' + clothes)

