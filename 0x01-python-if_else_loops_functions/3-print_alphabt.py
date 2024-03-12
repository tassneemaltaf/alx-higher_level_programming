#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if chr(i) == 'e' or chr(i) == 'z' :
        pass
    print("{:c}".format(i), end="")
