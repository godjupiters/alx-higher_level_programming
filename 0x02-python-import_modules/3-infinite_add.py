#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ans = sum(int(arg) for arg in sys.argv[1:])
    print(ans)
