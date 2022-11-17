# x = 3
#
#
# def func():
#     global x  # объявляем, что переменная является глобальной
#     print(x)
#     x = 5
#     x += 5
#     return x
#
#
# print(func())

# b4.3.2
# def multi(*nums):
#     result = 1
#     for n in nums:
#         result *= n
#     return result
#
# print(multi(5, 2, 3))

# palindrom
# def palindrom(text):
#     if len(text) <= 1:
#         return True
#     if text[0] != text[-1]:
#         return False
#     return palindrom(text[1:-1])
#
#
# print(palindrom('шалаш'))


# LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO -> L*I*t*B*e*o*F*L*c*S*G*B*O*F*Q*x*M*H*o*I*u*D*D*W*c*q*c*V*g*k*c*R*o*A*e*o*c*X*O
# def rec(text):
#     if len(text) == 1:
#         return text
#     if len(text) == 2:
#         return text[0] + '*' + text[1]
#     return text[0] + '*' + rec(text[1:-1]) + '*' + text[-1]
#
# text = input()
# print(rec(text))

# (((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo -> (((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqooqk))r)m))p)xs))s))imu)d)ktm))))))))y)d))))s))xlm)h)))m)v))e)v))wv)))))))e))))xk))y))p))t)))
# def rec(text):
#     if len(text) == 1:
#         if text == '(':
#             return text + ')'
#         else:
#             return text * 2
#     elif text[0] == '(':
#         return '(' + rec(text[1:]) + ')'
#     return text[0] + rec(text[1:]) + text[0]
#
#
# print(rec('(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo'))

# # b4.3.3
# def rec(n):
#     if n == 1:
#         return n
#     return n + rec(n - 1)
#
# print(rec(4))

# # b4.3.4
# def rec(text):
#     if len(text) == 1:
#         return text
#     return text[-1] + rec(text[:-1])
#
#
# text = 'abcdefg'
# print(rec(text))

# b4.3.5
def rec(number):
    if number < 10:
        return number
    return number % 10 + rec(number // 10)


print(rec(123))
