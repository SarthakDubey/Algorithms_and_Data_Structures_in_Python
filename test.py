def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        length, width = len(grid), len(grid[0])
        visited = set()
        queue = []

        def traverse(i, j):
            adjacent = [
                (i+di, j+dj) for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1))
                if 0 <= i+di < length and 0 <= j+dj < width and grid[i+di][j+dj] == '1'
            ]
            return adjacent
        
        print(traverse(0, 0))

        for i in range(length):
            for j in range(width):
                if grid[i][j] == "1" and (i, j) not in visited:
                    queue.append((i, j))
                    while queue:
                        current_i, current_j = queue.pop()
                        if (current_i, current_j) not in visited:
                            visited.add((current_i, current_j))
                        for a, b in traverse(current_i, current_j):
                            queue.append((a, b))
                    num_islands += 1

        return num_islands


numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])

