N = int(input())
time_diff_list = []
hour_output= []
minute_output = []
city_output= []
GMT_time = 0

for i in range(0,N):
    i_n = input().split(' ')
    time_diff_list.append(int(i_n[-1]))
    city_output.append(i_n[0])

city_and_time_inp = input()
city_inp_list = city_and_time_inp.split(' ')[0]
time_inp_list = city_and_time_inp.split(' ')[-1].split(':')

for j in range(len(city_output)):
    if city_output[j] == city_inp_list:
        GMT_time = int(time_inp_list[0]) - time_diff_list[j]
        break
 
for k in range(len(city_output)):
    if GMT_time >= 24:
        GMT_time_new = GMT_time -24
        if time_diff_list[k] < 0:
            hour_output.append(GMT_time + time_diff_list[k])
        else:
            hour_output.append(GMT_time_new + time_diff_list[k])
    else:
        hour_output.append(GMT_time + time_diff_list[k])
        
    print('{:02d}:{:02d}'.format(int(hour_output[k]),int(time_inp_list[-1])))

    