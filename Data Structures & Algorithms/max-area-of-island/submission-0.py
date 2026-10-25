class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False]*col for _ in range(row)]
        direction = [(0,1), (1,0), (0,-1),(-1,0)]

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0
            
            res = 1
            for d in direction:
                dr, dc = d[0], d[1]
                nr, nc = r+dr, c+dc
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                    visited[nr][nc] = True
                    res += dfs(nr, nc)
            
            return res

        maxArea = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    area = dfs(i, j)
                    if maxArea < area:
                        maxArea = area

        return maxArea