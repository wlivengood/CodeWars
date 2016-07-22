def winner(candidates):
    if len(candidates) != 3:
        return False
    for c in candidates:
        if len(c) != 2:
            return False
        if len(c['scores']) not in [1, 2]:
            return False
        for s in c['scores']:
            if s < 5 or s > 100 or s % 5 != 0:
                return False
        if not c['name']:
            return False
    eligible = [c for c in candidates if sum(c['scores']) <= 100]
    if not eligible:
        return False
    score_list = [sum(c['scores']) for c in eligible]
    winner = eligible[score_list.index(max(score_list))]
    return winner['name']