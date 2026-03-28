#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best = 0
    for key, value in a_dictionary.items():
        if best < a_dictionary[key]:
            best = a_dictionary[key]
            best_st = key 
    return best_st
