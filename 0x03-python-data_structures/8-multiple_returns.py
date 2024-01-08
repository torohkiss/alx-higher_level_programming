#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    l = len(sentence)
    c = sentence[0]

    return (l, c)
