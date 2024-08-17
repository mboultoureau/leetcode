class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> paths(m, vector<int>(n, 0));
        // Fill first row
        for (int i = 0; i < n; i++)
        {
            paths[0][i] = 1;
        }

        // Fill first col
        for (int i = 1; i < m; i++)
        {
            paths[i][0] = 1;
        }

        // Fill the rest
        for (int r = 1; r < m; r++)
        {
            for (int c = 1; c < n; c++)
            {
                paths[r][c] = paths[r - 1][c] + paths[r][c - 1];
            }
        }

        return paths[m - 1][n - 1];
    }
};