import itertools
def maximum_sub_array(array):
    min_sum, max_sum = 0, 0
    for running_sum in itertools.accumulate(array):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

def main():
    array = [904, 40, 523, 12, -335, -385, -124, 481, -31]
    print(maximum_sub_array(array))

if __name__ == '__main__':
    main()