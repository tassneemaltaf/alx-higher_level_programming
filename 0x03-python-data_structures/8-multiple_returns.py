#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ""):
        return ()
    length = len(sentence)
    first = sentence[0]
    tup = (length, first)
    return tup
