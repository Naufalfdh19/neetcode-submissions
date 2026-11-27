class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)*len(board[0]) < len(word):
            return False

        row, col = len(board), len(board[0])

        res = False
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*col for _ in range(row)]

        def backtrack(r, c, bucket, target, visited):
            nonlocal res

            # print(bucket)

            if len(bucket) == len(word):
                if bucket == target:
                    res = True
                return

            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if 0 <= nc < col and 0 <= nr < row and not visited[nr][nc]:
                    visited[nr][nc] = True
                    backtrack(nr, nc, bucket+board[nr][nc], target, visited)
                    visited[nr][nc] = False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    backtrack(i,j,word[0],word,visited)
        

        return res

            
            
