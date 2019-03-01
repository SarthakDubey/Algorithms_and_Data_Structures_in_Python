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

def find(array, edge):
    """
    Find the parent node of an edge and return it.
    """
    if array[edge] == -1:
        return edge
    else:
        find(array, array[edge])
    pass

def union(array, edge1, edge2):
    """
    Join the two edges together by making one the parent of another.
    """

    pass

def mst_kruskal(graph):
    """
    Find MST of a graph using kruskal's algorithm. Graph is expressed as a dictionary.
    """

    pass

class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent, rank, count, answer = {}, {}, 0, []
        # Implementing Union Find Rank

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(count, node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return count
            if rank[node2] > rank[node1]:
                parent2, parent1 = parent1, parent2
            rank[node1] += 1
            parent[node2] = node1
            count -= 1
            return count

        for i, j in positions:
            parent[(i, j)] = (i, j)
            rank[(i, j)] = 0
            count += 1
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if (x, y) in parent:
                    count = union(count, (i, j), (x, y))
            answer.append(count)
        print(answer)
        return answer


a = Solution()
# a.numIslands2(21,71,[[19,28],[14,38],[15,44],[17,12],[6,19],[11,69],[2,30],[7,43],[19,6],[7,29],[10,21],[17,55],[20,66],[12,28],[11,64],[12,52],[18,15],[2,52],[10,20],[0,50],[16,5],[17,25],[12,67],[6,45],[13,17],[5,55],[10,42],[20,17],[3,26],[20,61],[14,10],[9,1],[9,69],[6,29],[11,53],[3,66],[4,45],[12,65],[11,35],[5,67],[18,35],[2,57],[12,12],[13,53],[9,65],[13,0],[3,18],[13,39],[5,54],[20,43],[19,29],[17,37],[17,45],[3,38],[2,61],[2,65],[3,21],[5,40],[10,4],[12,36],[2,8],[3,33],[15,4],[13,35],[0,45],[20,29],[10,66],[19,7],[0,46],[19,11],[10,22],[19,0],[0,9],[2,20],[16,64],[10,37],[16,49],[4,20],[20,68],[10,38],[17,59],[15,54],[17,60],[19,18],[0,60],[9,62],[3,69],[10,44],[15,2],[14,44],[17,0],[18,42],[17,28],[11,10],[11,42],[11,67],[0,32],[8,0],[17,6],[7,26],[17,65],[17,66],[7,38],[8,17],[7,60],[0,16],[7,59],[18,8],[16,63],[7,0],[11,46],[0,7],[6,4],[2,63],[8,56],[18,18],[12,70],[2,15],[14,65],[13,52],[11,0],[10,48],[7,8],[11,44],[0,35],[4,64],[6,36],[16,17],[7,34],[1,33],[11,60],[17,11],[4,58],[4,9],[18,7],[15,40],[11,24],[17,3],[7,9],[1,38],[1,14],[15,21],[14,68],[14,69],[16,40],[5,60],[18,46],[15,51],[7,65],[1,34],[15,55],[19,63],[5,35],[20,9],[13,1],[20,69],[19,67],[17,44],[12,44],[10,49],[12,43],[14,21],[18,11],[11,9],[4,56],[6,70],[8,54],[1,55],[17,47],[18,38],[3,31],[16,37],[13,7],[15,6],[18,33],[4,60],[17,40],[7,3],[3,32],[13,41],[5,62],[17,4],[20,5],[15,32],[19,31],[8,69],[19,58],[3,35],[6,64],[0,37],[15,56],[6,46],[4,42],[4,51],[2,7],[7,13],[20,47],[10,29],[12,18],[20,52],[5,5],[12,34],[1,57],[7,32],[3,58],[14,29],[2,32],[2,46],[14,5],[3,9],[19,68],[18,16],[19,2],[6,23],[20,3],[10,69],[9,0],[0,13],[20,38],[6,14],[0,21],[6,50],[2,5],[1,20],[5,20],[1,5],[10,0],[7,6],[15,13],[8,21],[7,14],[9,9],[19,8],[13,25],[5,30],[1,16],[18,19],[16,44],[4,5],[15,37],[20,14],[20,8],[5,23],[13,44],[17,56],[13,62],[2,18],[1,58],[17,2],[20,40],[8,9],[8,52],[6,24],[19,65],[7,48],[20,51],[2,21],[7,39],[11,27],[7,22],[12,6],[19,12],[12,66],[0,55],[20,62],[11,20],[2,35],[2,0],[6,7],[5,41],[9,37],[8,44],[16,15],[9,48],[18,54],[19,52],[19,24],[19,46],[5,0],[19,50],[2,37],[18,31],[6,20],[4,59],[5,39],[9,38],[19,51],[3,67],[11,33],[7,57],[13,47],[20,64],[8,24],[13,69],[4,11],[4,46],[13,32],[18,3],[20,54],[18,17],[7,5],[15,12],[12,7],[6,11],[5,4],[17,26],[7,12],[12,68],[8,45],[8,2],[15,34],[12,20],[1,26],[6,54],[19,16],[0,17],[9,13],[4,65],[12,58],[11,52],[8,32],[18,32],[11,50],[9,50],[17,13],[11,17],[16,53],[18,26],[2,42],[14,58],[0,23],[19,44],[9,39],[15,47],[11,70],[10,35],[8,41],[15,39],[20,50],[2,50],[17,39],[1,28],[7,63],[16,61],[15,58],[19,17],[11,40],[20,46],[12,41],[6,32],[2,67],[4,52],[14,24],[0,43],[17,34],[6,56],[2,53],[1,69],[0,11],[16,48],[1,47],[14,12],[7,23],[8,37],[17,18],[7,27],[7,2],[10,63],[13,6],[3,23],[12,8],[1,52],[11,30],[9,57],[16,57],[9,58],[4,38],[18,36],[10,17],[20,24],[13,64],[18,37],[4,21],[17,33],[2,33],[15,10],[8,40],[14,52],[19,1],[2,45],[11,55],[3,40],[8,31],[20,57],[6,33],[6,22],[6,28],[2,11],[4,15],[4,31],[16,26],[9,27],[10,61],[5,52],[3,68],[0,19],[13,40],[0,52],[18,22],[1,24],[13,29],[12,33],[16,58],[19,66],[6,62],[18,40],[17,58],[2,34],[15,63],[8,23],[14,50],[20,16],[6,9],[8,1],[3,0],[20,10],[15,23],[1,0],[13,4],[8,25],[10,13],[12,9],[18,39],[3,24],[20,63],[16,39],[7,36],[15,65],[13,10],[19,20],[3,54],[12,35],[17,49],[17,31],[14,48],[18,65],[2,44],[9,51],[17,64],[16,36],[7,10],[5,9],[12,13],[6,59],[13,21],[8,14],[10,67],[20,56],[6,53],[18,25],[14,39],[8,70],[10,27],[0,48],[0,36],[12,56],[3,28],[15,14]])


a.numIslands2(3,3,[[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]])

def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    dummy = set()
    for i in s:
        dummy.add(i) if i not in dummy else dummy.remove(i)
    return len(dummy) <= 1

import heapq as hq
t = ["c", "a", "t"]
print(hq.heapify(t))
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
from itertools import groupby
[list(group) for key, group in groupby(sorted(words, key=sorted), sorted)]
