class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<int> onesRows(m, 0);
        vector<int> onesCols(n, 0);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    onesRows[i] += 1;
                    onesCols[j] += 1;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = onesRows[i] + onesCols[j] - (m - onesRows[i]) - (n - onesCols[j]);
            }
        }
        
        return grid;
    }
};