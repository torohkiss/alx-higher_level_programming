#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments")
    elif len(sys.argv) == 2:
        print("1 argument")
    else:
        print("{} arguments".format(len(sys.argv)-1))

    for i, v in enumerate(sys.argv):
        if v != sys.argv[0]:
            print("{}: {}".format(i, v))
