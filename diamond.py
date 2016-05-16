def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    else:
        midpoint = (n - 1)/2
        s = ""
        for i in range(n):
            stars = "*" * (n - int((abs(midpoint - i) * 2)))
            spaces = " " * int((abs(midpoint - i)))
            s += spaces + stars + "\n"
        return s
