class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False]*col for _ in range(row)]
        direction = [(0,1), (1,0), (0,-1),(-1,0)]

        def dfs(r, c):
            if grid[r][c] == '0':
                return 
            
            res = 0
            for d in direction:
                dr, dc = d[0], d[1]
                nr, nc = r+dr, c+dc
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                    visited[nr][nc] = True
                    dfs(nr, nc)

        totalIsland = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    totalIsland += 1

        return totalIsland 
                        
                
