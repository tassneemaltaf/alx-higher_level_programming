#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'z' :
        print("{:c}".format(i), end="")
