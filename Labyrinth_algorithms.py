from collections import namedtuple, deque

graph_namedtuple = namedtuple('graph', ('x', 'y'))

simplemaze = ([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


def simplemaze_to_adjacency_list(maze, verbose=0):
    if maze is None:
        assert ValueError("Maze empty")
    graph_dict = {(i, j): [] for j in range(len(maze[0]))
                  for i in range(len(maze)) if not maze[i][j]}
    if verbose:
        for i, j in graph_dict.keys():
            if i < len(maze) - 1 and not maze[i + 1][j]:
                graph_dict[(i, j)].append(('S', (i + 1, j)))
                graph_dict[(i + 1, j)].append(('N', (i, j)))
            if j < len(maze[0]) - 1 and not maze[i][j + 1]:
                graph_dict[(i, j)].append(('E', (i, j + 1)))
                graph_dict[(i, j + 1)].append(('W', (i, j)))
    else:
        for i, j in graph_dict.keys():
            if i < len(maze) - 1 and not maze[i + 1][j]:
                graph_dict[(i, j)].append((i + 1, j))
                graph_dict[(i + 1, j)].append((i, j))
            if j < len(maze[0]) - 1 and not maze[i][j + 1]:
                graph_dict[(i, j)].append((i, j + 1))
                graph_dict[(i, j + 1)].append((i, j))
    return graph_dict


def BFS(maze, start, goal):
    graph = simplemaze_to_adjacency_list(maze, 1)
    vertex_list = deque([('', start)])
    visited = set()
    while vertex_list:
        path, current = vertex_list.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbor in graph[current]:
            vertex_list.append((path + direction, neighbor))
    return "No Way Found"


def DFS(maze, start, goal):
    graph = simplemaze_to_adjacency_list(maze, 1)
    vertex_stack = deque([('', start)])
    visited = set()
    while vertex_stack:
        path, current = vertex_stack.pop()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbor in graph[current]:
            vertex_stack.append((path + direction, neighbor))
    return "No Way Found"

def Topological_sort_helper(graph, visited, i, stack):
    visited[i]=True
    for node in graph[i]:
        if visited[i]==False:
            Topological_sort_helper(graph, visited, node, stack)
    stack.insert(0, i)


def Topological_sort(graph):
    visited = False*len(graph)
    stack = []
    for i in range(len(graph)):
        if visited[i] == False:
            Topological_sort_helper(graph, visited, i, stack)
    print(stack)


print(BFS(simplemaze, (3, 1), (9, 10)))
print(DFS(simplemaze, (3, 1), (9, 10)))
