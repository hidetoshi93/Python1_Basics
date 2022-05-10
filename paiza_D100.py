# 10/10 testcase 

inp = input()
num_of_under = 0
num_of_haifun = 0
for i in inp:
    if i == '-':
        num_of_haifun += 1
    elif i == '_':
        num_of_under += 1

if num_of_haifun > num_of_under:
    print(inp.replace('_', '-'))
elif num_of_haifun <= num_of_under:
    print(inp.replace('-', '_'))