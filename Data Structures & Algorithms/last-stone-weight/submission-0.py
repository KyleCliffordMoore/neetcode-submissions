class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # flip for max proirity queue
        stones = [-i for i in stones]

        heapq.heapify(stones)

        while stones:
            largest = -heapq.heappop(stones)
            
            if not stones:
                return largest
            
            largest2 = -heapq.heappop(stones)


            heapq.heappush(stones, largest2 - largest)
        
        print("How did we get here?")
        return 0
