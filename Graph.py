# An attempt to build a graph class with basic functions to understand add, delete, BFS, DFS methods
import collections


class Graph(object):
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def _DFS(self, v, visited):
        visited[v] = True
        print('{}, '.format(v))
        for i in self.graph[v]:
            if visited[i] == False:
                self._DFS(i, visited)

    def DFS(self, v):
        visited = [False] * (len(self.graph))
        self._DFS(v, visited)


def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.DFS(2)


if __name__ == '__main__':
    main()
