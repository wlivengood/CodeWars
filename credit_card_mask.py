def maskify(cc):
    hashes = "#" * (len(cc) - 4)
    last_four = cc[-4:]
    masked_cc = hashes + last_four
    return masked_cc
