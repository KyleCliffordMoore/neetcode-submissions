class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                
                left_smaller = stack[-1] if stack else -1

                width = i - left_smaller - 1
                best = max(best, height * width)

            stack.append(i)

        return best