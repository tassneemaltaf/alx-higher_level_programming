#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quo = a / b
        return quo
    except ZeroDivisionError:
        quo = None
        return quo
    finally:
        print("Inside result: {}".format(quo))

