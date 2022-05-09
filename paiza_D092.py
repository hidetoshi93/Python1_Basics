from unittest import TestCase


# 10/10 TestCase

input_line1 = input().split(' ')
input_line2 = input().split(' ')


price1 = int(input_line1[2])/(int(input_line1[0])*int(input_line1[1]))
price2 = int(input_line2[2])/(int(input_line2[0])*int(input_line2[1]))

if(price1 < price2):
    print(f'{input_line1[0]} {input_line1[1]} {input_line1[2]}')
elif(price1 > price2):
    print(f'{input_line2[0]} {input_line2[1]} {input_line2[2]}')
else:
    print('DRAW')