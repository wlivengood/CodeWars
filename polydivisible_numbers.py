DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def to_base(x, b):
    if x == 0:
        return '0'
    digs = []
    while x > 0:
        digs.insert(0, DIGITS[x % b])
        x = x // b
    converted = "".join(digs)
    return converted

def to_dec(x, b):
    x = str(x)
    dec = 0
    digs = [DIGITS.index(i) for i in x]
    for i in range(len(digs)):
        dec += digs[i]*(b**(len(x) - i - 1))
    return dec

def is_polydivisible(s, b):
    s = str(s)
    for i in range(len(s)):
        if to_dec(s[:i+1], b) % (i + 1) != 0:
            return False
    return True

def get_polydivisible(n, b):
    polydiv, i = 0, 0
    while True:
        if is_polydivisible(to_base(i, b), b):
            polydiv += 1
        if polydiv == n:
            return to_base(i, b)
        i += 1
