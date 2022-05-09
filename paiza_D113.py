from unittest import TestCase


# 10/10 TestCase

input_line = input().split(':')
print(input_line)
if(int(input_line[0]) - 8) >= 0:
    print(f'{(int(input_line[0]) - 8)}:{input_line[-1]}')
else:
    print(f'{(int(input_line[0]) - 8 + 24)}:{input_line[-1]}')