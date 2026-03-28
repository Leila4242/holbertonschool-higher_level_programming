#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = []
    if len(set_1) > len(set_2):
        main_set = list(set_1)
    else:
        main_set = list(set_2)
    for i in range(len(main_set)):
        if main_set[i] in set_1 and main_set[i] in set_2:
            c_set.append(main_set[i])
    return c_set
