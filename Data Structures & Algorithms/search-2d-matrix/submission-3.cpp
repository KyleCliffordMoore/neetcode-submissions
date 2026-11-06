class Solution {
public:

    int getLength(vector<vector<int>>& matrix) {
        int colLength = matrix.size();
        int rowLength = matrix[0].size();

        return colLength * rowLength;
    }

    int getValue(vector<vector<int>>& matrix, int idx) {
        
        int colLength = matrix.size();
        int rowLength = matrix[0].size();

        int rowIdx = idx / rowLength;
        int colIdx = idx - (rowIdx * rowLength);

        return matrix[rowIdx][colIdx];
    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int left = 0;
        int right = getLength(matrix) - 1;

        while (left <= right) {
            int mid = (right - left) / 2 + left;

            if (target == getValue(matrix, mid))
                return true;

            if (target < getValue(matrix, mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }

        }

        return false;

    }
};
