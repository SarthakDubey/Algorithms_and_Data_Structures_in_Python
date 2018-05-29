def dutch(A, i):
    pivot = A[i]
    beginning, middle, end = 0, 0, len(A)
    while middle < end:
        if A[middle] < pivot:
            A[beginning], A[middle] = A[middle], A[beginning]
            beginning, middle = beginning + 1, middle + 1
        elif A[middle] == pivot:
            middle += 1
        else:
            end -= 1
            A[middle], A[end] = A[end], A[middle]
    return A, pivot


def main():
    result, pivot = dutch([1, 4, 5, 2, 3, 7, 2, 5, 2, 7, 8,
                           2, 5, 7, 2, 1, 8, 3, 6, 3, 8, 4, 2, 9, 0, 2, 6], 2)
    print(result, pivot)


if __name__ == '__main__':
    main()
