#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maximum = list(a_dictionary.keys())[0]
    maximum_v = a_dictionary[maximum]
    for i, j in a_dictionary.items():
        if j > maximum_v:
            maximum = i
    return maximum
