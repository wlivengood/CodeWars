def three_dig(x):
    ONES = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ",
            "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ",
            "eighteen ", "nineteen "]
    TENS = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    y = x
    hund_dig = y//100
    y = y%100
    tens_dig = y//10
    if tens_dig == 1:
      tens_dig = 0
      ones_dig = y
    else:
      ones_dig = y%10
string = ONES[hund_dig]
    if x > 99:
      string += "hundred "
string += TENS[tens_dig] + ONES[ones_dig]
return string

def int_to_english(n):
    MAGNITUDES = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ",
                  "sextillion ", "septillion "]
    answer = ""
    n = str(n)
    first_group = n[:(len(n) + 2)%3 + 1]
    answer += three_dig(int(first_group))
    answer += MAGNITUDES[(len(n) - 1)//3]
    n= n[(len(n) + 2)%3 + 1:]
    while len(n):
        answer += three_dig(int(n[:3]))
        answer += MAGNITUDES[(len(n) - 1)//3]
        n = n[3:]
    return answer.strip()