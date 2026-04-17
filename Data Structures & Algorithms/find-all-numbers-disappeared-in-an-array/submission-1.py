class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        noAppears = set([i + 1 for i in range(len(nums))])

        for num in nums:
            if num in noAppears:
                noAppears.remove(num)
        
        return list(noAppears)