def sum_pairs(ints, s):
    new_ints = []
    [new_ints.append(int) for int in ints if new_ints.count(int) <2]
    pairs = []
    i_j_pairs = []
    for i in range(len(new_ints)):
        for j in range((i + 1), len(new_ints)):
            if new_ints[i] + new_ints[j] == s:
                pairs.append([new_ints[i], new_ints[j]])
                i_j_pairs.append([i, j])
    if pairs != []:
        answer = pairs[0]
        for k in range(len(pairs)):
            if i_j_pairs[k][1] < i_j_pairs[pairs.index(answer)][1]:
                answer = pairs[k]
        return answer
    else:
        return None
