class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []

        phoneMap = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz", '0': "+"
        }

        curr = ""
        ans = []

        def backtrack(idx):
            nonlocal curr
            nonlocal ans

            if len(curr) == len(digits):
                ans.append(curr[:])

            if idx >= len(digits):
                return

            digit = digits[idx]
            for letter in phoneMap[digit]:
                curr += letter
                backtrack(idx + 1)
                curr = curr[:-1]

        backtrack(0)
        return ans