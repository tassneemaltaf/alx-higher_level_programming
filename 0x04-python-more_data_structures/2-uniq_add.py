#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    add = 0
    for i in range(0, len(my_list)):
        if i != 0:
            if my_list[i] == my_list[i - 1]:
                continue
            else:
                add += my_list[i]
        else:
            add += my_list[i]
    return add
