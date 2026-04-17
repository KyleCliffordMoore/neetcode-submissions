class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        mySet = set(nums)
        
        # Get starters 
        starters = []
        for num in mySet:
            if num - 1 not in mySet:
                starters.append(num)

        maxium = -1
        for start in starters:
            count = 1
            while start + count in mySet:
                count += 1
            maxium = max(maxium, count)

        return maxium