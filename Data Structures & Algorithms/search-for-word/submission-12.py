class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        curr = ""

        def inBounds(i, j):
            if i >= len(board):
                return False
            if i < 0:
                return False
            if j >= len(board[0]):
                return False
            if j < 0:
                return False
            return True


        def backtrack(i, j, prev):
            nonlocal curr

            print(curr)

            if len(curr) >= len(word):
                
                if curr == word:
                    ans = curr
                    return True
                # print(curr)
                return False
            
            if inBounds(i - 1, j) and (i - 1, j) not in prev:
                curr += board[i - 1][j]
                prev.add( (i - 1, j) )
                t = backtrack(i - 1, j, prev)
                if t:
                    return True
                prev.remove( (i - 1, j) )
                curr = curr[:-1]

            if inBounds(i + 1, j) and (i + 1, j) not in prev:
                curr += board[i + 1][j]
                prev.add( (i + 1, j) )
                t = backtrack(i + 1, j, prev)
                prev.remove( (i + 1, j) )
                if t:
                    return True
                curr = curr[:-1]

            if inBounds(i, j - 1) and (i, j - 1) not in prev:
                curr += board[i][j - 1]
                prev.add( (i, j - 1) )
                t = backtrack(i, j - 1, prev)
                if t:
                    return True
                prev.remove( (i, j - 1) )
                curr = curr[:-1]

            if inBounds(i, j + 1) and (i, j + 1) not in prev:
                curr += board[i][j + 1]
                prev.add( (i, j + 1) )
                t = backtrack(i, j + 1, prev)
                if t:
                    return True
                prev.remove( (i, j + 1) )
                curr = curr[:-1]
            
            return False

        for mi in range(len(board)):
            for mj in range(len(board[0])):
                curr = board[mi][mj]
                prev = set()
                prev.add( (mi, mj) )
                # print(prev, curr, mi, mj)
                t = backtrack(mi, mj, prev)
                if t:
                    return True

        # print("ans", ans )
        return False