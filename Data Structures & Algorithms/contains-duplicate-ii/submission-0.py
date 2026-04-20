class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        currChars = set()

        k+= 1

        for char in nums[:k]:
            if char in currChars:
                return True
            currChars.add(char)
        
        for i in range(k, len(nums)):
            currChars.remove(nums[i - k])

            if nums[i] in currChars:
                return True
            currChars.add(nums[i])
        
        return False