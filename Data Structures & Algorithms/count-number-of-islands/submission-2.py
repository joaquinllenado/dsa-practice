class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        seen = set()
        islands = 0

        def bfs(r,c):
            seen.add((r,c))
            q = deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r,c) not in seen:
                        seen.add((r,c))
                        q.append((r,c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1

        return islands