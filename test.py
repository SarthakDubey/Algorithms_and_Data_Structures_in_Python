import math


def num_of_ways(n, m):
    a, b, c = math.factorial(
        m + n - 2), math.factorial(m - 1), math.factorial(n - 1)
    d = b * c
    e = a / d
    return e


print(num_of_ways(5, 5))
