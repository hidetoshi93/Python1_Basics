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

hinata_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
input_line = input().split(' ')
input_line = [int(k) for k in input_line]
input_line_new = []
for j in range (0, len(input_line)-1):
    if j == 0:
        input_line_new.append(input_line[j])
    else:
        value = input_line[j-1] + input_line[j]
        input_line_new.append(value)

for i in range (len(hinata_list)):
        print(hinata_list[i], end="")
        if (i+1) in input_line_new:
            print()
    
