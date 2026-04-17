class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        smallest = float('inf')
        small = float('inf')
        largest = float('-inf')
        large = float('-inf')

        for num in nums:
            if num < smallest:
                small = smallest
                smallest = num
            elif num < small:
                small = num
            
            if num > largest:
                large = largest
                largest = num
            elif num > large:
                large = num
        
        return largest * large - smallest * small