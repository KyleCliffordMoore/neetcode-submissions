class Solution:

    def descTwoSum(self, target, nums, start, ans):
        a = -target
        left = start
        right = len(nums) - 1
        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ == target:

                ans.append([a, nums[left], nums[right]])

                # remove duplicates
                lval = nums[left]
                while left < right and nums[left] == lval:
                    left += 1
                rval = nums[right]
                while left < right and nums[right] == rval:
                    right -= 1

            if sum_ < target:
                left += 1
            if sum_ > target:
                right -= 1


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        for i, a in enumerate(nums):

            # duplicate check
            if i > 0 and a == nums[i - 1]:
                continue
            
            target = -a
            self.descTwoSum(target, nums, i + 1, ans)


        return ans