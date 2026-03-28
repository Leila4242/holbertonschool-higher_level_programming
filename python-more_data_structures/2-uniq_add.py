#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for i in range(len(my_list)-1):
        if i is not uniq_list:
            uniq_list.append(i)
    sum = 0
    for i in uniq_list:
        sum += i
    return sum
