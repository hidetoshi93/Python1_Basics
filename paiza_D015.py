from unittest import TestCase


# 10/10 testcase

n = int(input())
list = []
for i in range(1,n+1):
    list.append(i)

list = sorted(list, reverse = True)
for j in list:
    print(j)
