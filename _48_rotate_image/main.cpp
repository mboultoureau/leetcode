class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const size_t n = matrix.size();

        for (size_t row = 0; row < n / 2; ++row) {
            for (size_t col = 0; col < (n + 1) / 2; ++col) {
                swap(matrix[row][col], matrix[col][n - row - 1]);
                swap(matrix[row][col], matrix[n - row - 1][n - col - 1]);
                swap(matrix[row][col], matrix[n - col - 1][row]);
            }
        }
    }
};