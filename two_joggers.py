def nbr_of_laps(x, y):
    gcd = max([i for i in range(1, min(x,y) + 1) if (x % i == 0 and y % i == 0)])
    laps_x, laps_y = y//gcd, x//gcd
    return [laps_x, laps_y] 
