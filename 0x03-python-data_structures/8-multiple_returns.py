#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    c = sentence[0]

    if not sentence:
        c = None

    return (l, c)
