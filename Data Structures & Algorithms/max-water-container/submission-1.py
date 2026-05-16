class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        left_ptr = 0
        right_ptr = len(heights) - 1

        while left_ptr < right_ptr:

            x = right_ptr - left_ptr 
            y = min(heights[left_ptr], heights[right_ptr])

            max_area = max(max_area, x * y)

            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_area