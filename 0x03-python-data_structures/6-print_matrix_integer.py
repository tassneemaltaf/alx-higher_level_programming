#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nums in matrix:
        for num in nums:
            print("{}".format(num), end=" " if num != nums[-1] else "") 
        print()
