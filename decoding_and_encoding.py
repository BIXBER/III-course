from operator import index
from itertools import groupby

def decoding(input_list = (input("\nВведите буквы и количество их повторений соответственно через пробел без запятых: ")).split()):
    
    list_of_simbols = []
    list_of_nums = []
    symbol_to_number = {}
    output_list = ""
    n = 0

    for i in input_list:
        if int(input_list.index(i)) % 2 == 0: 
            list_of_simbols.append((input_list[input_list.index(i)]).upper())
        else:
            list_of_nums.append(int(input_list[input_list.index(i)]))

    for i in list_of_simbols:
        symbol_to_number[i] = list_of_nums[n]
        n += 1
        for q, w in symbol_to_number.items():
            element = q * 1
            r = 0
            while r != w:
                output_list += f"{element} "
                r += 1
        del symbol_to_number[i]

    output_list =  output_list.split()

    return f"{output_list}"

print(f"\nРаскодированный список: {(decoding())}\n")



def encoding(input_list = (input("Введите буквы без пробелов и запятых в случайном порядке: "))):
    coding_list = list(input_list.upper())
       
    coding_list = [list(j) for i, j in groupby(coding_list)]
    symbol_to_count = {}
    output_list = []

    for i in coding_list:
        symbol_to_count[coding_list[coding_list.index(i)][0]] = len(i)
        for i, q in symbol_to_count.items():
            output_list.append(f"'{i}' = {q}")
        del symbol_to_count[i]
        
    output_list = "[" + ", ".join(output_list) + "]"
         
    return output_list

print(f"\nЗакодированный список: {encoding()}\n")

input("Нажмите 'Enter' для закрытия программы: ")