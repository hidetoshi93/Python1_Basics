# a = 10
# b = a ** 2
# c = b % 20 + 5
# d = 8
# e = d / b
# f = d // c
# print ('{0}, {1}'.format(e, f))



# a = "She said,\"He" + 3 * "y" + "!"
# b = "How are you?\" "
# print (a, b)


# Zen = 'NowIsBetterThanNever'
# print('{}{}{}{}'.format(Zen[5], Zen[10], Zen[-7], Zen[-3:-1]))


# Zen = 'SimpleIsBetterThanComplex'
# Zen[:1000] + 'J'


# a, b = 0, 1
# while b < 10:
#     print(b, end=',')
#     a, b = b, a+b

inp = int(input())
out = 0
for i in range(1, inp):
    out = i*inp
    print(f'{out} ', end = '')