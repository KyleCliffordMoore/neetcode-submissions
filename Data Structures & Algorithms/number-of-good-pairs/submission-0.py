class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0

        numbers = {}

        for num in nums:
            if num in numbers:
                pairs += numbers[num]
                numbers[num] += 1
            else:
                numbers[num] = 1
        
        return pairs