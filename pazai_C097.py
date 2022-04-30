
inp = input()
inp_list = inp.split(' ')
result_list = []

for i in range (0,int(inp_list[0])):
    if (i+1) % int(inp_list[1]) == 0 and (i+1) % int(inp_list[2])  == 0:
        result_list.append('AB')
    elif (i+1) % int(inp_list[1]) == 0:
        result_list.append('A')
    elif (i+1) % int(inp_list[2]) == 0:
        result_list.append('B')
    else:
        result_list.append('N')


for j in result_list:
    print(j)