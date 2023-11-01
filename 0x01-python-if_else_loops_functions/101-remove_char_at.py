#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        str = str[0:n] + str[n+1:]
    return str





102-magic_calculation.py


#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    return a * b - c
