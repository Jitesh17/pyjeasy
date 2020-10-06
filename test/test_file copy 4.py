import os
from sys import exit as x
import itertools
import numpy as np
import pandas as pd
import statistics #import mode
import printj
from tqdm import tqdm
from collections import Counter 
  
  
def new_pattern(n, l, result: bool, verbose: bool=True):
    if len(l) > 9:
        # print(l)
        list_all = [li for (li, x) in l]
        # list5 = list_all[-5:]
        list5 = []
        list5.append(list_all[0])
        # list5.append(list_all[1])
        # list5.append(list_all[2])
        # # list5.append(list_all[3])
        # list5.append(list_all[4])
        # # list5.append(list_all[5])
        # list5.append(list_all[6])
        list5.append(list_all[7])
        list5.append(list_all[8])
        list5.append(list_all[9])
        if n in list5:
            if verbose:
                printj.green('new_pattern: Win')
            return True
        else:
            if verbose:
                printj.red('new_pattern: Lose')
            return False
    else:
        return False  
    
def is_n_in_last_5(n, l, verbose: bool=True):
    if len(l) > 6:
        # print(l)
        list_all = [li for (li, x) in l]
        list5 = list_all[-5:]
        if n in list5:
            if verbose:
                printj.green('     Least Frequent')
            return True
        else:
            if verbose:
                printj.red('     Most Frequent')
            return False
    else:
        return False
    
def is_in_fixed_numbres(n, l, verbose: bool=True):
    # if len(l) > 9:
    # print(l)
    # list_all = [li for (li, x) in l]
    # list5 = list_all[-5:]
    list5 = l
    if n in list5:
        if verbose:
            printj.green('Win')
        return True
    else:
        if verbose:
            printj.red('Lose')
        return False
  
def is_even(n, verbose: bool=True):
    if n%2 == 0:
        if verbose:
            printj.green('is_even')
        return True
    else:
        if verbose:
            printj.red('is_odd')
        return False
  
def is_big(n, verbose: bool=True):
    if n>4:
        if verbose:
            printj.green('is_big')
        return True
    else:
        if verbose:
            printj.red('is_small')
        return False
    
def frequency(input): 
  
    # Convert given list into dictionary 
    # it's output will be like {'ccc':1,'aaa':3,'bbb':2} 
    # dict = Counter(input) 
  
    # # Get the list of all values and sort it in ascending order 
    # value = sorted(dict.values(), reverse=True) 
  
    # # Pick second largest element 
    # secondLarge = value[1] 
  
    # # Traverse dictionary and print key whose 
    # # value is equal to second large element 
    # for (key, val) in dict.iteritems(): 
    #     if val == secondLarge: 
    #         print( key )
    #         return key
    c = Counter(input)
    # print(c.most_common()[1][0])
    # print(c.most_common())
    # return c.most_common()[1][0]
    return c.most_common()
        
    
def frequency_last_n_turns(input, last_n: int=20): 
  
    # Convert given list into dictionary 
    # it's output will be like {'ccc':1,'aaa':3,'bbb':2} 
    # dict = Counter(input) 
  
    # # Get the list of all values and sort it in ascending order 
    # value = sorted(dict.values(), reverse=True) 
  
    # # Pick second largest element 
    # secondLarge = value[1] 
  
    # # Traverse dictionary and print key whose 
    # # value is equal to second large element 
    # for (key, val) in dict.iteritems(): 
    #     if val == secondLarge: 
    #         print( key )
    #         return key
    if len(input)>last_n:
        c = Counter(input[-last_n:])
        return c.most_common()
    else:
        return [(0,0)]
    # print(c.most_common()[1][0])
    # print(c.most_common())
    # return c.most_common()[1][0]
    # return c.most_common()
        
        
def find_max_mode(list1):
    list_table = statistics._counts(list1)
    len_table = len(list_table)

    if len_table == 1:
        max_mode = statistics.mode(list1)
        return max_mode
    else:
        new_list = []
        for i in range(len_table):
            new_list.append(list_table[i][0])
        max_mode = max(new_list) # use the max value here
        return new_list
    # return max_mode

def top_n_dict(full_dict, n):
    return {k: full_dict[k] for k in list(full_dict)[:n]}

def count_consecutive(test_list):
    c_list = []
    c_dict = dict()
    last_e = None # any is ok
    count = 1
    fort = 0
    test_list.append(None) # anything other than true or false is ok
    for i, e in enumerate(test_list):
        if last_e == e:
            count += 1
        else:
            c_list.append(count)
            fort += 1
            c_dict[fort] = count
            count = 1
        last_e = e
    return c_list, c_dict


def possible5():
    digits = np.arange(10)
    possible5=[]
    for L in range(0, len(digits)+1):
        for subset in itertools.combinations(digits, L):
            # print(subset) 
            if len(subset) == 5:
                possible5.append(subset)
    # print(possible5)      
    # print(subset)      
    return possible5


def choose5(list_target_num):
    df = pd.DataFrame(data=[],
                    #   columns = ['no', 
                    #                 #  'time',
                    #                 'n_TenThousands', 
                    #                 'n_Thousands', 'n_Hundreds',
                    #                 'n_Tens',
                    #                 'n_Ones', 
                    #                 ]
                      )
    row = dict()
    all_possible_combos = possible5()
    max_val = -1
    for numbers in tqdm(all_possible_combos):
        # row = dict()
        # printj.yellow(numbers)
        result_list = []
        for target_num in list_target_num:
            # printj.yellow(numbers)
            result = is_in_fixed_numbres(target_num, list(numbers), verbose=False)
            result_list.append(result)
            # printj.red(result)
        count_consecutive_list, c_dict = count_consecutive(result_list)
        # row[str(numbers)] = max(count_consecutive_list[1:])
        row[str(numbers)] = count_consecutive_list[-1]
        if max_val < row[str(numbers)]:
            max_val = row[str(numbers)]
            max_number = numbers
    df = df.append(pd.DataFrame(row, index =['max(count_consecutive_list)']) )
    printj.yellow(df.T)
    printj.purple(max_number)
    # filter_col = [col for col in df if df[col]['max(count_consecutive_list)']==max_val]
    for col in df:
        if df[col]['max(count_consecutive_list)']==max_val:
            print(col)
    # printj.purple(filter_col)
    printj.purple(max_val)
    # printj.purple(max(row))
    # (max(count_consecutive_list[1:])
    # return possible5
    
    

f = open("/home/jitesh/JG/my_projects/pyjeasy/test/data.txt", "r")
# print(f.read())
df = pd.DataFrame(data=[],columns = ['no', 
                                    #  'time',
                                    'n_TenThousands', 
                                    'n_Thousands', 'n_Hundreds',
                                    'n_Tens',
                                    'n_Ones', 
                                    ])
for i, data in enumerate(f):
    d = data.replace('\\n','')
    # if i <3:
    #     printj.blue(d)
    if i%7 == 0:
        no = int(d)
        row = dict()
        row["no"] = no
    if i%7 == 1:
        time = d
        # row["time"] = time
    if i%7 == 2:
        n_TenThousands = d
        row["n_TenThousands"] = int(d)
    if i%7 == 3:
        n_Thousands = d
        row["n_Thousands"] = int(d)
    if i%7 == 4:
        n_Hundreds = d
        row["n_Hundreds"] = int(d)
    if i%7 == 5:
        n_Tens = d
        row["n_Tens"] = int(d)
    if i%7 == 6:
        n_Ones = d
        row["n_Ones"] = int(d)
        # printj.cyan(row)
        df = df.append(pd.DataFrame(row, index =[time]) )
        if i <20:
            continue
        # printj.cyan(frequency(df["n_TenThousands"]))
        # printj.green(row["n_TenThousands"])
# reversed_df = df[:50].iloc[::-1]
reversed_df = df.iloc[::-1]
# reversed_df = df
gap_1_list = []
count_1 = 0
last_num = 11
result = False
n_TenThousands_list = []

combo_test_list_dict = dict()
combo_count_consecutive_list_dict = dict()
combo_result = dict()
all_possible_combos = possible5()
for combo in all_possible_combos:
    # printj.red(f'{str(combo)}')
    combo_result[str(combo)]= []
    combo_test_list_dict[str(combo)]= []
    combo_count_consecutive_list_dict[str(combo)]= []
# printj.red(f'{combo_count_consecutive_list_dict}')
# x()
# test_list = []
# type_list = ["big-small", "even-odd"]
max_dict = dict()
last_consi_dict = dict()
last_consi_ratio_dict = dict()
# test_list_dict = dict()
# count_consecutive_list_dict = dict()
# for _type in type_list:
#     test_list_dict[_type]= []
#     count_consecutive_list_dict[_type]= []
for num in reversed_df["n_TenThousands"]:
    
    if num == 1:
        if last_num== num:
            count_1 += 1
        else:
            count_1 = 1
            
    else:
        count_1 = 0
    gap_1_list.append(count_1)
    last_num = num
    # printj.yellow(num)
    # result = is_n_in_last_5(num, frequency(n_TenThousands_list))
    # printj.yellow(frequency_last_n_turns(n_TenThousands_list, 20))
    # result = is_n_in_last_5(num, frequency_last_n_turns(n_TenThousands_list, 40))
    # result = is_in_fixed_numbres(num, [1,4,8,9,3])
    # result = new_pattern(num, frequency(n_TenThousands_list), result)
    # result = is_big(num)
    # test_list.append(result)
    for combo in all_possible_combos:
        combo_result[str(combo)] = is_in_fixed_numbres(num, list(combo), verbose=False)
        combo_test_list_dict[str(combo)].append(combo_result[str(combo)])
    
    # is_big_result = is_big(num)
    # test_list_dict["big-small"].append(is_big_result)
    # is_even_result = is_even(num)
    # test_list_dict["even-odd"].append(is_even_result)
    
    n_TenThousands_list.append(num)            ################## Impoertant ##################
    # printj.cyan.on_white(frequency(n_TenThousands_list))
    # choose5(n_TenThousands_list)
    # printj.yellow(num)
    # printj.green(row["n_TenThousands"])
# printj.yellow(test_list)
# printj.cyan(test_list_dict)
# printj.green(test_list_dict["even-odd"]==test_list)
# choose5(n_TenThousands_list)

for combo in all_possible_combos:
    count_consecutive_list, c_dict= count_consecutive(combo_test_list_dict[str(combo)])
    combo_count_consecutive_list_dict[str(combo)] = {"list": count_consecutive_list, "dict": c_dict}
    max_dict[str(combo)] = max(combo_count_consecutive_list_dict[str(combo)]["list"])
    last_consi_dict[str(combo)] = combo_count_consecutive_list_dict[str(combo)]["list"][-1]
    last_consi_ratio_dict[str(combo)] = round(last_consi_dict[str(combo)]/max_dict[str(combo)], 3)
# printj.green(count_consecutive_list_dict["even-odd"]["list"])
# printj.green(count_consecutive_list_dict["even-odd"]["dict"])
# printj.purple(f'max_dict: {max_dict}')
# printj.yellow(f'last_consi_dict: {last_consi_dict}')

sorted_last_consi_dict = {k: v for k, v in sorted(last_consi_dict.items(), key=lambda item: item[1], reverse = True)}
printj.green(f'sorted_last_consi_dict: {top_n_dict(sorted_last_consi_dict, 20)}')

sorted_last_consi_ratio_dict = {k: v for k, v in sorted(last_consi_ratio_dict.items(), key=lambda item: item[1], reverse = True)}
# printj.yellow(f'sorted_last_consi_dict: {sorted_last_consi_ratio_dict}')
# sorted_last_consi_ratio_dict={k: sorted_last_consi_ratio_dict[k] for k in list(sorted_last_consi_ratio_dict)[:20]}
printj.cyan(f'sorted_last_consi_dict: {top_n_dict(sorted_last_consi_ratio_dict, 20)}')
# count_consecutive_list, c_dict = count_consecutive(test_list)
# printj.green(count_consecutive_list)
# printj.green(c_dict)
# printj.yellow(f'max: {max(count_consecutive_list[1:])}')
# limit = 3
# for i, d in enumerate(count_consecutive_list):
#     if i%2==1 and d >limit:
        
#         printj.red(d)
#     if i%2==0 and d >limit:
        
#         printj.green(d)
# # printj.green(possible5())

# choose5(n_TenThousands_list) ####################### look in 

# printj.green(df)
# printj.purple(df["n_TenThousands"])
# # lst = row["n_TenThousands"]
# # maxi = max(set(lst), key=lst.count)
# printj.yellow(f'Most frequent = {find_max_mode(df["n_TenThousands"])}')
# frequency(df["n_TenThousands"])
# possible5()
