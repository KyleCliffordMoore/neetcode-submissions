class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        def inBounds(idx):
            return 0 <= idx < len(flowerbed)

        def canPlace(idx):

            left = idx - 1
            right = idx + 1
            if inBounds(left) and inBounds(right):
                return [0, 0, 0] == flowerbed[left:right + 1]
            if inBounds(left):
                return [0, 0] == flowerbed[left:right]
            if inBounds(right):
                return [0, 0] == flowerbed[idx:right + 1]
            return flowerbed[idx] == 0

        for i in range(len(flowerbed)):
            if canPlace(i):
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0