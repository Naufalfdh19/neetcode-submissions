class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        level = 0
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j,level))
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]

        while q:
            r, c = q[0][0], q[0][1]
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 1:
                        level = q[0][2]+1
                        grid[nr][nc] = 2
                        q.append((nr,nc,level))
            q.popleft()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return level
