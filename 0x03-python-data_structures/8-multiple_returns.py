#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ""):
        first = None
    length = len(sentence)
    first = sentence[0]
    tup = (length, first)
    return tup
