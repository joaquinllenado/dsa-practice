class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, seen, cur):
            if row not in range(ROWS) or col not in range(COLS) or heights[row][col] < cur or (row, col) in seen:
                return
            
            seen.add((row, col))

            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                dfs(r, c, seen, heights[row][col])
                    
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r,c in pac:
            if (r,c) in atl:
                res.append([r,c])
        
        return res