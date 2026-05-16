class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []

        pos = 0
        neg = 0

        searchingForPos = True
        while pos <= len(nums) and neg <= len(nums):
            
            if searchingForPos:
                while pos < len(nums) and nums[pos] < 0:
                    pos += 1
                if pos < len(nums):
                    ans.append(nums[pos])
                pos += 1
            else:
                while neg < len(nums) and nums[neg] > 0:
                    neg += 1
                if neg < len(nums):
                    ans.append(nums[neg])
                neg += 1
            searchingForPos = not searchingForPos

        return ans               