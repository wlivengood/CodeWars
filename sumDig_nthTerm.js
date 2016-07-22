def sumDig_nthTerm(initVal, patternL, nthTerm):
    li = [initVal]
    while len(li) < nthTerm:
        for item in patternL:
            li.append(li[-1] + item)
    answer = li[nthTerm - 1]
    answer_sum = 0
    for i in str(answer):
        answer_sum += int(i)
    return answer_sum