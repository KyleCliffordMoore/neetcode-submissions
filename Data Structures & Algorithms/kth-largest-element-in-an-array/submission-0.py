class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        myheap = []
        
        for num in nums:
            heapq.heappush(myheap, num)
            if len(myheap) > k:
                heapq.heappop(myheap)
        
        return myheap[0]