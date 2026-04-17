class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curr = []
        ans = []

        def backtrack(index):
            nonlocal curr
            nonlocal ans

            print(curr)
            ans.append(curr.copy())

            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()


        backtrack(0)

        return ans