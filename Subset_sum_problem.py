def subset_sum(array, target):
    bool_dparray = [[False for _ in range(target+1)]
                    for _ in range(len(array))]
    for i in range(len(bool_dparray)):
        bool_dparray[i][0] = True
    for i in range(1, len(bool_dparray)):
        for j in range(1, len(bool_dparray[0])):
            if j < array[i-1]:
                bool_dparray[i][j] = bool_dparray[i-1][j]
            else:
                bool_dparray[i][j] = bool_dparray[i-1][j -
                                                       array[i-1]] or bool_dparray[i-1][j]
    return bool_dparray[i][j]
#Since all numbers are true we necessarily don't need a 2-d List

def subset_sum_1d(array, target):
    #Coin analogy
    dp_array = [None for _ in range(target+1)]
    dp_array[0] = []
    for value in array:
        for i in range(target-value, -1, -1):
            if dp_array[i] is not None:
                dp_array[i+value] = dp_array[i] + [value]
    print(dp_array)
    return dp_array[-1] 

if __name__ == '__main__':
    example = [3, 34, 4, 12, 5, 2]
    target = 36
    print(subset_sum(example, target))
    print(subset_sum_1d(example, target))

