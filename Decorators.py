#Decorators
#Hàm trang trí

import time

def cal_time(func):
    print('Start decorators a')
    def timer(*args, **kwargs):
        print('Start decorators b')
        start_time = time.time()
        result = func(*args, **kwargs)
        print(*args)
        print(**kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} took {(end_time-start_time)*1000} ms')
        return result
    return timer

@cal_time
def cal_square(numbers):
    print('Start cal_square')
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@cal_time
def cal_cube(numbers):
    print('Start cal_cube')
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

arrray = range(1,10000)
out_square = cal_square(arrray)
out_cube = cal_cube(arrray)
