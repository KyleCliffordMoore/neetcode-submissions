class Solution:
    
    def get2DCoords(self, i, row_len):
        return (i // row_len, i % row_len)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Empty Matrix Edge Case
        if len(matrix) == 0:
            return False

        # Normal Case
        # (row, col) = self.get2DCoords(7, len(matrix[0]))
        row_len = len(matrix[0])
        col_len = len(matrix)

        left = 0
        right = row_len * col_len - 1

        while left <= right:
            mid = (left + right) // 2
            (mrow, mcol) = self.get2DCoords(mid, row_len)

            if target == matrix[mrow][mcol]:
                return True
            elif target < matrix[mrow][mcol]:
                right = mid - 1
            else:
                left = mid + 1


        return False
