class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        constexpr int modulo = 12345;
        int n = grid.size();
        int m = grid[0].size(); // 1 <= grid.length
        vector<vector<int>> result(n, vector<int>(m));

        long long suffix = 1;
        for (int r = n - 1; r >= 0; --r)
        {
            for (int c = m - 1; c >= 0; --c)
            {
                result[r][c] = suffix;
                suffix = (suffix * grid[r][c]) % modulo;
            }
        }

        long long prefix = 1;
        for (int r = 0; r < n; ++r)
        {
            for (int c = 0; c < m; ++c)
            {
                result[r][c] = (result[r][c] * prefix) % modulo;
                prefix = (prefix * grid[r][c]) % modulo;
            }
        }

        return result;
    }
};