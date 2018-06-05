def levenshtein(string1, string2):
    levenshtein_map = [[0 for _ in range(len(string2) + 1)]
                       for _ in range(len(string1) + 1)]

    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if i == 0:
                levenshtein_map[i][j] = j
            elif j == 0:
                levenshtein_map[i][j] = i
            elif string1[i - 1] == string2[j - 1]:
                levenshtein_map[i][j] = levenshtein_map[i - 1][j - 1]
            else:
                levenshtein_map[i][j] = min(
                    levenshtein_map[i - 1][j], levenshtein_map[i][j - 1],
                    levenshtein_map[i - 1][j - 1]) + 1

    return levenshtein_map[len(string1)][len(string2)]


def main():
    string1 = "saturday"
    string2 = "sunday"
    print(levenshtein(string1, string2))


if __name__ == '__main__':
    main()
