#!/usr/bin/python3

def magic_calculation(a, b):
    ans = 0

    for z in range(1, 3):
        try:
            if z > a:
                raise Exception('Too far')
            ans += a ** b / z
        except Exception:
            ans = b + a
            break
    return ans
