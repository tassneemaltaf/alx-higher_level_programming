#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            v = my_list_1[i] / my_list_2[i]
        except TypeError:
            v = 0
            print("wrong type")
        except ZeroDivisionError:
            v = 0
            print("division by 0")
        except IndexError:
            print("out of range")
            v = 0
        finally:
            new_list.append(v)
    return new_list
