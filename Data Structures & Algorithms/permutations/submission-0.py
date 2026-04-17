class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        curr = nums
        def backtrack(idx):

            
            print(curr, idx)
            if idx == len(curr):
                ans.append(curr.copy())

            for i in range(idx, len(curr)):
                curr[i], curr[idx] = curr[idx], curr[i]
                backtrack(idx + 1)
                curr[i], curr[idx] = curr[idx], curr[i]

        backtrack(0)
        return ans