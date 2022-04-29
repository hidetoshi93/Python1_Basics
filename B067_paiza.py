# 10/10 testcase but algorithm not true line 27

schelde_input = []
N = 0
while ( 1 >= N or 100 >= N):
    N = int(input())
    break

for i in range(0,N):
    i_n = input().split(' ')
    if(int(i_n[2]) - int(i_n[1]) >=0 and (int(i_n[2]) - int(i_n[1]) <= 1000)):
        if (int(i_n[1]) <= int(i_n[2])) and (int(i_n[0]) <= (int(i_n[2]) - int(i_n[1]) + 1)):
            schelde_input.append(i_n)

is_check = True

condition_ness_day = []
condition_start_day = []
condition_end_day = []

for n in schelde_input:
    condition_ness_day.append(int(n[0]))
    condition_start_day.append(int(n[1]))
    condition_end_day.append(int(n[-1]))

if sum(condition_ness_day) <= (max(condition_end_day)-min(condition_start_day) + 1):
    if((condition_start_day[-1] + condition_start_day[-1]) <= condition_end_day[-1]):
        is_check = True
    else:
        is_check = False
else:
    is_check = False
    
if is_check == True:
    print("YES")
else:
    print("NO")