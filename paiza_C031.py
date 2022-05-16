# 0/10 TestCase
N = int(input())
city_GMT_dic = {}

for i in range(0,N):
    city_and_GMT = input().strip().split(' ')
    # city_GMT_dic[key] = value
    city_GMT_dic[city_and_GMT[0]] = int(city_and_GMT[1])
    
inp_city_localtime = input().strip().split(' ')
city_name = inp_city_localtime[0]
local_hour_inp = int(inp_city_localtime[1].strip().split(':')[0])
local_min_inp = int(inp_city_localtime[1].strip().split(':')[1])

for city_GMT in city_GMT_dic.items():
    local_GMT_time = 0
    local_time = 0
    if city_GMT_dic[city_name] < city_GMT[1]:
        local_GMT_time = city_GMT[1] - city_GMT_dic[city_name]
    else:
        local_GMT_time = city_GMT_dic[city_name] - city_GMT[1]
        local_GMT_time = 24 - local_GMT_time

    local_time = local_hour_inp + local_GMT_time

    if local_time >= 24:
        local_time -= 24

    print(format(local_time, '02') + ":" + format(local_min_inp, '02'))



    # print('{:02d}:{:02d}'.format(int(hour_output[k]),int(time_inp[-1])))

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