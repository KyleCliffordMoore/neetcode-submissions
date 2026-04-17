class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing = None

        for i in range(len(nums) - 1):
            left = nums[i]
            right = nums[i + 1]

            if left < right:
                if increasing == False:
                    return False
                if increasing == None:
                    increasing = True
            
            if left > right:
                if increasing:
                    return False
                if increasing == None:
                    increasing = False
        
        return True
