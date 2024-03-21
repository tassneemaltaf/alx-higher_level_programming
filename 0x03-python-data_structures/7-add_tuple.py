#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 2:
        tuple_a -= (0,) * (len(tuple_a) - 2)
    elif len(tuple_b) > 2:
        tuple_b -= (0,) * (len(tuple_b) - 2)
    else:
        len_dif = len(tuple_a) - len(tuple_b)
        if len_dif > 0:
            tuple_b += (0,) * len_dif
        elif len_dif < 0:
            tuple_a += (0,) * len_dif
        return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
