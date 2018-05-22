def no_of_score_combinations(score, points, table={}):
    table = [0 for _ in range(0, score+1)]
    table[0]=1
    for point in points:
        for score_n in range(point, score+1):
            table[score_n] += table[score_n - point]
    return table[score]

print(no_of_score_combinations(20, (3,5,10)))