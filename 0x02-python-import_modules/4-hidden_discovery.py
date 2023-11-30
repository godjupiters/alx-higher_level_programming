#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    ns = dir(hidden_4)
    for n in ns:
        if n[:2] != "__":
            print(n)
