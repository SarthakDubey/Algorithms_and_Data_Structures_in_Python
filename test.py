import math

def num_of_ways(n, m):
    a, b, c = math.factorial(
        m + n - 2), math.factorial(m - 1), math.factorial(n - 1)
    d = b * c
    e = a / d
    return e


print(num_of_ways(5, 5))


import heapq as hq

listed = [1, 3, 5, 7, 9]
tupled = (1, 3, 5, 7, 9)
dictionary = {1, 3, 5, 7, 9}
sets = set()
sets.add(1)
hq.heapify(listed)
print(hq.nlargest(1, listed))
#hq._heapify_max(listed)
print(hq.heappop(listed))
from collections import defaultdict

alpha = defaultdict(list)
alpha[1] = 20
from collections import Counter


x = {'foo':'bar'}
y = {'baz': x}
z = y['baz']['foo']
print(z)