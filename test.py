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

inp = input().split(' ')
inp_list = [int(i) for i in inp]

if len(inp_list[0] % inp_list[1]) != 0:
    tree_num = int(inp_list[0]/inp_list[1]) + 1
    print(inp_list[2] * tree_num )
else:
    tree_num = int(inp_list[0]/inp_list[1])
    print(inp_list[2] * tree_num)