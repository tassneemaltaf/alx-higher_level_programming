#!/usr/bin/python3
def uppercase(str):
    result = ""
    for s in str:
        code = ord(s)
        dif = 122 - ord(s)
        if code >= 97 and code <= 122:
            result += chr(90-dif)
        else:
            result += s
    print(result)
