def longest_palindrome (s):
    max_len = 0
    i = 0
    while i <= len(s) - 1:
        j = i + 1
        while j <= len(s):
            substring = s[i:j]
            reverse = substring[::-1]
            if reverse == substring:
                if len(substring) >= max_len:
                    max_len = len(substring)
            j += 1
        i += 1
    return max_len
