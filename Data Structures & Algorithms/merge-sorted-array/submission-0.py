class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = len(nums2) - 1
        final = len(nums1) - 1

        ans = nums1

        while left >= 0 and right >= 0:
            
            if nums1[left] >= nums2[right]:
                ans[final] = nums1[left]
                left -= 1
            else:
                ans[final] = nums2[right]
                right -= 1

            final -= 1
        
        while left >= 0:
            ans[final] = nums1[left]
            left  -= 1
            final -= 1

        while right >= 0:
            ans[final] = nums2[right]
            right -= 1
            final -= 1

        # print(nums1)
        # print(nums2)
