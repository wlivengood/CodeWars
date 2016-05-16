def find_outlier(integers):
    even_counter, odd_counter = 0, 0
    for i in integers[:3]:
        if i % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    if even_counter > 1:
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i
