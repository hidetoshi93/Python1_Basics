# 10/10 testcase
# in khoảng trắng giữa các số

inp = int(input())
out = 0
for i in range(1, 10):
    out = i*inp
    if i == 9:
        print(f'{out}', end = '')
    else:
        print(f'{out} ', end = '')