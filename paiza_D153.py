from unittest import TestCase


# 10/10 TestCase

input_line = input().split(' ')
input_line_new = []
for i in input_line:
    input_line_new.append(int(i))
print(input_line)

for j in input_line_new:
    if j != min(input_line_new) and j != max(input_line_new):
        print(j)
        break