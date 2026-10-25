class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        
        for i in range(n):
            seenRow = set()
            seenCol = set()
            for j in range(m):
                if board[i][j] in seenRow:
                    return False
                if board[j][i] in seenCol:
                    return False

                if board[i][j] != ".":
                    seenRow.add(board[i][j])
                if board[j][i] != ".":
                    seenCol.add(board[j][i])
 
        for i in range(0,n,3):
            for j in range(0,n,3):
                seen = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] in seen:
                            return False
                        if board[k][l] != ".":                    
                            seen.add(board[k][l])

        return True
            