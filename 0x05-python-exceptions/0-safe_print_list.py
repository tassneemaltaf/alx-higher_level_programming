#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for num in my_list:
            if count < x:
                print("{:d}".format(num), end="")
                count += 1
        print()
        return count
    except Exception:
        return 0
