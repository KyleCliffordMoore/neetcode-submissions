class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            found = False
            greater = -1

            for val in nums2:
                if val == num:
                    found = True
                elif found and val > num:
                    greater = val
                    break

            ans.append(greater)

        return ans