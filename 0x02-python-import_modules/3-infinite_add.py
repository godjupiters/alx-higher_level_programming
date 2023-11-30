#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    ans = 0
    for i in sys.argv:
        ans += int(i)
        print("{:d}".format(ans))
