#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    n = len(roman_string)
    for i in range(n):
        current_val = roman_numerals.get(roman_string[i], 0)
        if i + 1 < n and current_val < roman_numerals.get(roman_string[i+1], 0):
            result -= current_val
        else:
            result += current_val
    return result
