class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            left_height = heights[left]
            right_height = heights[right]

            max_area = max(max_area, min(left_height, right_height) * width)

            if left_height > right_height:
                right -= 1
            else:
                left += 1
        
        return max_area