def get_anagrams(s):
    if len(s) <= 1:
        return s
    else:
        anagrams = []
        for j in get_anagrams(s[1:]):
            for i in range(len(s)):
                anagrams.append(j[:i] + s[0:1] + j[i:])
        return anagrams
        
def get_words(hash_of_letters):
    s = ""
    for key, value in hash_of_letters.items():
        for c in value:
            s += c * key
    anagrams = list(set(get_anagrams(s)))
    anagrams.sort()
    return anagrams