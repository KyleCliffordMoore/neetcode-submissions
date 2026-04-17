class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        def helper_printHeap(myHeap):
            while myHeap:
                print(heapq.heappop(myHeap), end=' ')

        def calcDist(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return ( (x1 - x2)**2 + (y1 - y2)**2 ) ** (1/2)

        myHeap = []
        for point in points:
            dist = calcDist(point, (0, 0))
            heapq.heappush(myHeap, (-dist, point))
            if len(myHeap) > k:
                heapq.heappop(myHeap)
                
        ans = [d for (i, d) in myHeap]

        return ans
        # helper_printHeap(myHeap)

        
