#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for num in my_list:
            if count <= x:
                if type(num) is not int:
                    pass
                else:
                    print("{}".format(num), end="")
                count += 1
            else:
                raise IndexError
        print()
    except IndexError:
        print("list index out of range")
