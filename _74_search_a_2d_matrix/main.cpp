class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Treat the matrix as an array
        int m = matrix.size();
        int n = matrix[0].size();

        int left = 0;
        int right = m * n - 1;

        while (left <= right) {
            int middle = (left + right) / 2;
            int value = matrix[middle / n][middle % n];
            if (value == target) {
                return true;
            } else if (value > target) {
                right = middle - 1;
            } else {
                left = left + 1;
            }
        }

        return false;


        // OTHER SOLUTION: find the row with binary search + find the column with binary search
    }
};