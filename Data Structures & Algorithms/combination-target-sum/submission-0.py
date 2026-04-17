class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        

        ans = []
        curr = []
        def backtrack(idx):

            # print(idx, curr)

            if target - sum(curr) == 0:
                ans.append(curr.copy())
            if target - sum(curr) < 0:
                return
            
            for i in range(idx, len(nums)):
                # print('no run?')
                curr.append(nums[i])
                backtrack(i)
                curr.pop()
        
        backtrack(0)
        return ans