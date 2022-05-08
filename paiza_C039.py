def convert_symbol_to_num(str):
    dic = {'/': 1, '<' : 10}
    list_val = list(dic.values())
    list_key = list(dic.keys())
    if str[0] == '-':  
        inp_val =(-1)*(str.count(list_key[0])*list_val[0] + str.count(list_key[1])*list_val[1])
    else: 
        inp_val =(str.count(list_key[0])*list_val[0] + str.count(list_key[1])*list_val[1])
    return inp_val

def calculate_inp(str):
    str = str.replace('+', ' +')
    str = str.replace('-', ' -')
    str_li = str.split(' ')
    sum = 0
    for i in str_li:
        i_val = convert_symbol_to_num(i)
        sum += (i_val)
    return sum

inp_str = input()
calculate_inp(inp_str)
