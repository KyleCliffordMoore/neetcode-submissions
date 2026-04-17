class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            toReturn = []
            lidx, ridx = 0, 0

            while lidx < len(left) and ridx < len(right):
                if left[lidx] < right[ridx]:
                    toReturn.append(left[lidx])
                    lidx += 1
                else:
                    toReturn.append(right[ridx])
                    ridx += 1
            
            if lidx < len(left):
                toReturn += left[lidx:]
            if ridx < len(right):
                toReturn += right[ridx:]
            
            return toReturn
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)
        
        return mergeSort(nums)

