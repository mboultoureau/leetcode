class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        const size_t m = grid.size();
        const size_t n = grid[0].size();

        int rowFlipped = 0;
        int colFlipped = 0;

        for (size_t r = 0; r < m; ++r) {
            for (size_t c = 0; c < n; ++c) {
                if (c < n - 1 - c && grid[r][c] != grid[r][n - c - 1]) rowFlipped++;
                if (r < m - 1 - r && grid[r][c] != grid[m - r - 1][c]) colFlipped++;
            }
        }

        return min(rowFlipped, colFlipped);   
    }
};