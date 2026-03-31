class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        max_area = 0
        cur = 0

        def bfs(r, c):
            q = deque()
            seen.add((r,c))
            q.append((r,c))
            nonlocal cur
            while q:
                row, col = q.pop()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in seen:
                        cur += 1
                        q.append((r,c))
                        seen.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    bfs(r,c)
                    seen.add((r,c))
                    cur += 1
                    max_area = max(max_area, cur)
                    cur = 0

        return max_area