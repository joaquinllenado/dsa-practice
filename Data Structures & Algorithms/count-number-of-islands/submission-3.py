class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
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
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in seen:
                        seen.add((r,c))
                        q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1

        return islands