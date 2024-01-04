#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    h_names = dir(hidden_4)
    for h in h_names:
        if h[0:2] != "__":
            print("{}".format(name))
