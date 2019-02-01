# Dynamic Programming.
# Fibonacci
def fib(n, cache={}):
    """
    A top-down approach to caching intermediate results,
    where the data is computed and saved to be called 
    multiple times from the call stack
    """
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

fib(9)

def maxsubarraysum(array):
    """
    Keep track of current sum and check if it's not getting negative (Subset sum problem)
    Further compare current sum with maximum sum, change if current sum improves.
    """
    current_max = 0
    maximum = 0
    for i in array:
        current_max += i
        current_max = 0 if current_max < 0 else current_max
        maximum = max(maximum, current_max)
    return maximum

maxsubarraysum([904, 40, 523, 12, -335, -385, -124, 481, -31])

def scorecombination(scores, total):
    """
    To find number of ways to the total, we start counting up to the total.
    Eg: Number of ways to 1, then 2, 3, 4, 5 and so forth
    """
    dp_array = [0 for _ in range(total+1)]
    for score in scores:
        for index in range(score, total+1, score):
            dp_array[index] = dp_array[index-score] + 1
    print(dp_array)
    return dp_array[~0]

scorecombination([2, 3, 7], 12)


class LRUCache(dict):
	def __init__(self, cap):
		self.remaining = cap

	def get(self, key):
		if key not in self:
			return -1
		val = self.pop(key)  # pop and re-insert to keep the order
		self[key] = val
		return val

	def put(self, key, value):
		if key in self:
			self.pop(key)
		else:
			if self.remaining > 0:
			    self.remaining -= 1
			else:
			    # cache is full, remove least recently used key which is the first key
			    self.pop(next(iter(self)))
		self[key] = value

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
# returns 1
cache.put(3, 3)
# evicts key 2
cache.get(2)
# returns - 1 (not found)
cache.put(4, 4)
# evicts key 1
cache.get(1)
# returns - 1 (not found)
cache.get(3)
# returns 3
cache.get(4)
# returns 4

def bfs(graph, start, end):
    """
    Basic breadth first search in a graph expressed as a dictionary.
    """
    from collections import deque
    queue = deque()
    visited = set()
    queue.append(start)
    while queue:
        # Pop left in queue equates to FIFO
        current = queue.popleft()
        if current == end:
            return True
        if current in visited:
            continue
        visited.add(current)
        for i in graph[current]:
            queue.append(i)
    return False

def dfs(graph, start, end):
    """
    Basic depth first search in a graph expressed as a dictionary.
    """
    from collections import deque
    queue = deque()
    visited = set()
    queue.append(start)
    while queue:
        # Pop in queue equates to LIFO
        current = queue.pop()
        if current == end:
            return True
        if current in visited:
            continue
        visited.add(current)
        for i in graph[current]:
            queue.append(i)
    return False

def bfs_matrix(graph, start, end):
    """
    Basic breadth first search in a graph expressed as a matrix.
    """
    from collections import deque
    queue = deque()
    visited = set()
    queue.append(start)
    directions = [(1, 0), (-1, 0), (0,1), (0, -1)]
    while queue:
        # Pop left in queue equates to FIFO
        i, j = queue.popleft()
        if (i, j) == end:
            return True
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for a, b in directions:
            if graph[i+a][j+b] == 1:
                queue.append((a+i, b+j))
    return False


def dfs_matrix(graph, start, end):
    """
    Basic breadth first search in a graph expressed as a matrix.
    """
    from collections import deque
    queue = deque()
    visited = set()
    queue.append(start)
    directions = [(1, 0), (-1, 0), (0,1), (0, -1)]
    while queue:
        # Pop left in queue equates to LIFO
        i, j = queue.pop()
        if (i, j) == end:
            return True
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for a, b in directions:
            if graph[i+a][j+b] == 1:
                queue.append((a+i, b+j))
    return False


# Kruskal's MST

def union(edge1, edge2):
    """
    Join the two edges together by making one the parent of another.
    """
    pass

def find(edge):
    """
    Find the parent node of an edge and return it.
    """
    pass

def mst_kruskal(graph):
    """
    Find MST of a graph using kruskal's algorithm. Graph is expressed as a dictionary.
    """
    
    pass


















