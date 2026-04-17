class Solution:

    def trap(self, heights: List[int]) -> int:
        
        start = 0
        stop  = 0
        sum_area = 0
        inter_sum_heights = 0

        while stop < len(heights):
            if heights[stop] >= heights[start]:
                height = min(heights[start], heights[stop])
                width = stop - start - 1
                if width > 0:
                    sum_area += width * height - inter_sum_heights
                    # print(start, stop, width * height, width, height)
                start = stop
                inter_sum_heights = 0
            elif stop != start:
                inter_sum_heights += heights[stop]

            stop += 1
        
        # print(sum_area)
        start = len(heights) - 1
        stop = len(heights) - 1
        inter_sum_heights = 0

        while stop > -1:
            
            if heights[stop] > heights[start]:
                # print(stop)
                height = min(heights[start], heights[stop])
                width = start - stop - 1
                if width > 0:
                    sum_area += width * height - inter_sum_heights
                    # print(start, stop, width * height, width, height, inter_sum_heights)
                start = stop
                inter_sum_heights = 0
            elif stop != start:
                inter_sum_heights += heights[stop]

            stop += -1

        return sum_area

