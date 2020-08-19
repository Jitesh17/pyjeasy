import os, sys

import numpy as np
import pandas as pd
import statistics #import mode
import printj
from collections import Counter 
  
  
def new_pattern(n, l, result: bool):
    if len(l) > 9:
        # print(l)
        list_all = [li for (li, x) in l]
        # list5 = list_all[-5:]
        list5 = []
        list5.append(list_all[0])
        list5.append(list_all[1])
        list5.append(list_all[2])
        # # list5.append(list_all[3])
        # list5.append(list_all[4])
        # # list5.append(list_all[5])
        # # list5.append(list_all[6])
        # list5.append(list_all[7])
        list5.append(list_all[8])
        list5.append(list_all[9])
        if n in list5:
            printj.green('new_pattern: Win')
            return True
        else:
            printj.red('new_pattern: Lose')
            return False
    else:
        return False  
    
def is_n_in_last_5(n, l):
    if len(l) > 9:
        # print(l)
        list_all = [li for (li, x) in l]
        list5 = list_all[-5:]
        if n in list5:
            printj.green('     Least Frequent')
            return True
        else:
            printj.red('     Most Frequent')
            return False
    else:
        return False
    
def is_in_fixed_numbres(n, l):
    # if len(l) > 9:
    # print(l)
    # list_all = [li for (li, x) in l]
    # list5 = list_all[-5:]
    list5 = l
    if n in list5:
        printj.green('Win')
        return True
    else:
        printj.red('Lose')
        return False
  
def is_even(n):
    if n%2 == 0:
        printj.green('is_even')
        return True
    else:
        printj.red('is_odd')
        return False
  
def is_big(n):
    if n>4:
        printj.green('is_big')
        return True
    else:
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

def count_consecutive(test_list):
    c_list = []
    c_dict = dict()
    last_e = False
    count = 0
    fort = 0
    for i, e in enumerate(test_list):
        if last_e == e:
            count += 1
        else:
            c_list.append(count)
            fort += 1
            # if fort%
            c_dict[fort] = count
            count = 0
        last_e = e
    return c_list, c_dict

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
test_list = []
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
    printj.yellow(num)
    result = is_n_in_last_5(num, frequency(n_TenThousands_list))
    result = is_in_fixed_numbres(num, [1,4,8,9,3])
    result = new_pattern(num, frequency(n_TenThousands_list), result)
    test_list.append(result)
    is_even(num)
    is_big(num)
    n_TenThousands_list.append(num)
    printj.cyan(frequency(n_TenThousands_list))
    # printj.yellow(num)
    # printj.green(row["n_TenThousands"])
count_consecutive_list, c_dict = count_consecutive(test_list)
printj.green(count_consecutive_list)
printj.green(c_dict)
printj.green(f'max: {max(count_consecutive_list[1:])}')
for i, d in enumerate(count_consecutive_list):
    if i%2==0 and d >4:
        
        printj.red(d)
# printj.green(df)
# printj.purple(df["n_TenThousands"])
# # lst = row["n_TenThousands"]
# # maxi = max(set(lst), key=lst.count)
# printj.yellow(f'Most frequent = {find_max_mode(df["n_TenThousands"])}')
# frequency(df["n_TenThousands"])
