class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        needsPair = set()

        for num in nums:
            if num in needsPair:
                needsPair.remove(num)
            else:
                needsPair.add(num)
        
        return len(needsPair) == 0