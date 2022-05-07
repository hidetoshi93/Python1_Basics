# 10/10 testcase

list = []
for i in range (0, 9):
    list.append(2**i)

print(list)
n = int(input())
if (n in list):
    print("OK")
else:
    print("NG")