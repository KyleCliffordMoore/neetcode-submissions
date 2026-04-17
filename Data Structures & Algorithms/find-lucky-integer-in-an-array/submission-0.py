class Solution:
    def findLucky(self, arr: List[int]) -> int:

        freq = Counter(arr)

        largest = -1
        for key, value in freq.items():
            if key == value:
                largest = max(largest, key)
        
        return largest

