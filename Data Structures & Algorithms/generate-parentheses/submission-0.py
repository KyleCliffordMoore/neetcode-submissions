class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        curr = ""
        ans = []

        def backtrack(openn, closedn):
            nonlocal curr
            nonlocal ans

            if openn + closedn == 2 * n:
                ans.append(curr[:])
            
            if openn < n:
                curr += '('
                backtrack(openn + 1, closedn)
                curr = curr[:-1]
            
            if closedn < openn:
                curr += ')'
                backtrack(openn, closedn + 1)
                curr = curr[:-1]

        backtrack(0, 0)
        return ans