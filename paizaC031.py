from unittest import TestCase


# 0/10 TestCase
N = int(input())
time_diff_list = []
hour_output= []
city_output= []
time_output = 0

for i in range(0,N):
    i_n = input().split(' ')
    time_diff_list.append(int(i_n[-1]))
    city_output.append(i_n[0])

city_and_time_inp = input()
city_inp_list = city_and_time_inp.split(' ')[0]
time_inp_list = city_and_time_inp.split(' ')[-1].split(':')

if int(time_inp_list[0]) == 0:
    time_inp_list[0] = 24
    

for j in range(len(city_output)):
    if city_output[j] == city_inp_list:
        if int(time_inp_list[0]) >= int(time_diff_list[j]):
            GMT_time = int(time_inp_list[0]) - time_diff_list[j]
        else:
            GMT_time = int(time_inp_list[0]) + time_diff_list[j]
        break

for k in range(len(city_output)):
    
    time_output = GMT_time + time_diff_list[k]
    if time_output < 24:
        hour_output.append(time_output)
    else:
        while True:
            time_output = time_output - 24
            if(time_output >= 0 and time_output < 24):
                break
        hour_output.append(time_output)
    print('{:02d}:{:02d}'.format(int(hour_output[k]),int(time_inp_list[-1])))
