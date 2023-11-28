#!/usr/bin/python3
def uppercase(str):
    ans = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        ans += char
    print(ans)
