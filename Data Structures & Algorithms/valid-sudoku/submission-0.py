class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board))]
        sqrs = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                
                val = board[i][j]
                if val == ".":
                    continue
                
                sqr_i = i // 3
                sqr_j = j // 3

                if val in rows[i] or val in cols[j] or val in sqrs[sqr_i][sqr_j]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                sqrs[sqr_i][sqr_j].add(val)
        
        return True
