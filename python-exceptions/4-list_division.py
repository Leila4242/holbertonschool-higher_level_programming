#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    count = 0
    while count < list_length:
        try:
            elm = my_list_1[count] / my_list_2[count]
            new_list.append(elm)
        except IndexError:
            new_list.append(0)
            print("out of range")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        finally:
            count += 1
    return new_list
