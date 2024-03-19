#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    length = len(sentence)
    if (sentence != ""):
        first = sentence[0]
    tup = (length, first)
    return tup
