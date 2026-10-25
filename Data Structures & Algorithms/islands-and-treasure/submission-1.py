from collections import deque
import copy

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        visited = [[False]*col for _ in range(row)]
        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(srcR, srcC, visited):
            level = 0
            q = deque([(srcR, srcC, level)])
            visited[srcR][srcC] = True

            while q:
                currLevel = q[0][2]+1
                for dr in direction:
                    r, c = q[0][0], q[0][1] 
                    dr, dc = dr[0], dr[1]
                    nr, nc = r+dr, c+dc

                    if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                        if grid[nr][nc] != -1:
                            visited[nr][nc] = True
                            q.append([nr, nc, currLevel])
                
                r, c, level = r, c, level = q.popleft()
            
                if level != 0:
                    if grid[r][c] > level:
                        grid[r][c] = level
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    visitedCopy = copy.deepcopy(visited)
                    bfs(i, j, visitedCopy)


            
            
