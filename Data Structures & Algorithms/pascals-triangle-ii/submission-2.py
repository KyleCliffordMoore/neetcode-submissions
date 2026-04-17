class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 1:
            return [1]
        
        prev = [1]
        for i in range(0, rowIndex):
            
            row = [1]
            for i in range(len(prev) - 1):
                left = prev[i]
                right = prev[i + 1]

                row.append(left + right)
            row.append(1)
            prev = row
        return row