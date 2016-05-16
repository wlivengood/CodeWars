def solution(digits):
    dig_str = str(digits)
    max_num = int(dig_str[0:5])
    for i in range(len(dig_str) - 4):
        num = int(dig_str[i:i + 5])
        if num > max_num:
            max_num = num
    return max_num
