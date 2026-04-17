class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        curr = []
        ans = []

        def backtrack(idx):
            print(curr)
            ans.append(curr[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return ans