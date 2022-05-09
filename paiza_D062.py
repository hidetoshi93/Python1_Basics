# 10/10 testcase

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