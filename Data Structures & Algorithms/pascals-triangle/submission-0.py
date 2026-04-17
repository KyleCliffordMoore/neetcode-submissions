class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        tri = [[1]]
        def genLayer(triangle):
            
            newLayer = [1]
            lastLayer = triangle[-1]
            for i in range(len(lastLayer) - 1):
                newLayer.append(lastLayer[i] + lastLayer[i + 1])
            newLayer.append(1)

            triangle.append(newLayer)
        
        for i in range(numRows - 1):
            genLayer(tri)
        return tri