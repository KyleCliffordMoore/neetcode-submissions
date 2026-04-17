class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        INCREASING, DECREASING, EQUAL = (0, 1, 2)

        mode = EQUAL

        for i in range(len(nums) - 1):
            left = nums[i]
            right = nums[i + 1]

            if left < right:
                if mode == DECREASING:
                    return False
                if mode == EQUAL:
                    mode = INCREASING
            
            if left > right:
                if mode == INCREASING:
                    return False
                if mode == EQUAL:
                    mode = DECREASING
        
        return True
