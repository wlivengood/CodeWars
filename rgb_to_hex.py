def rgb(r, g, b):
    dec_lst = [r, g, b]
    for i in range(len(dec_lst)):
        if dec_lst[i] < 0:
            dec_lst[i] = 0
        if dec_lst[i] > 255:
            dec_lst[i] = 255
    hex_lst = map(hex, dec_lst)
    remove_leading = [item.replace("0x", "") for item in hex_lst]
    padded_lst = ["0" + item if len(item) < 2 else item for item in remove_leading]
    hex_str = "".join(padded_lst)
    upper_hex_str = hex_str.upper()
    return upper_hex_str
