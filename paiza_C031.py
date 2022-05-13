# 0/10 TestCase
N = int(input())
time_diff_list = []
hour_output= []
city_output= []
city_inp_time_diff = 0

for i in range(0,N):
    i_n = input().split(' ')
    time_diff_list.append(int(i_n[-1]))
    city_output.append(i_n[0])

city_and_time_inp = input()
city_inp = city_and_time_inp.split(' ')[0]
time_inp = city_and_time_inp.split(' ')[-1].split(':')

if int(time_inp[0]) == 0:
    time_inp[0] = 24
    

for j in range(len(city_output)):
    if city_output[j] == city_inp:
        city_inp_time_diff = time_diff_list[j]
        break

for k in range(len(city_output)):
    time_output = int(time_inp[0]) - (city_inp_time_diff - time_diff_list[k])
    if time_output < 24:
        hour_output.append(time_output)
    else:
        while True:
            time_output = time_output - 24
            if(time_output >= 0 and time_output < 24):
                break
        hour_output.append(time_output)
    print('{:02d}:{:02d}'.format(int(hour_output[k]),int(time_inp[-1])))

# l = {}

# for i in range(int(input())):
#     a = input().strip().split(" ")
#     l[a[0]] = int(a[1])
# print(l)
# c = input().strip().split(" ")
# name = c[0]
# t = c[1].strip().split(":")
# t = list(map(int, t))   # int変換

# for aa in l.items():
#     m = 0
#     print(l[name])
#     print(aa)
#     if l[name] < aa[1]:
#         m = aa[1] - l[name]

#     else:
#         m = l[name] - aa[1]
#         m = 24-m

#     m = t[0] + m
    
#     if m >= 24:
#         m -= 24

#     print(format(m, '02') + ":" + format(t[1], '02'))