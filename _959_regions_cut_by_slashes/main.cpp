class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        vector<vector<bool>> expanded(n * 3, vector<bool>(n * 3, false));
        vector<vector<bool>> visited(n * 3, vector<bool>(n * 3, false));

        for (int r = 0; r < n; r++)
        {
            for (int c = 0; c < n; c++)
            {
                if (grid[r][c] == '/') {
                    expanded[r * 3][c * 3 + 2] = true;
                    expanded[r * 3 + 1][c * 3 + 1] = true;
                    expanded[r * 3 + 2][c * 3] = true;
                } else if (grid[r][c] == '\\') {
                    expanded[r * 3][c * 3] = true;
                    expanded[r * 3 + 1][c * 3 + 1] = true;
                    expanded[r * 3 + 2][c * 3 + 2] = true;
                }
            }
        }

        int count = 0;
        for (int r = 0; r < n * 3; r++)
        {
            for (int c = 0; c < n * 3; c++)
            {
                if (visited[r][c] == false && expanded[r][c] == false)
                {
                    dfs(expanded, visited, r, c, n);
                    count += 1;
                }
            }
        }

        return count;
    }

    void dfs(vector<vector<bool>>& expanded, vector<vector<bool>>& visited, int r, int c, int n)
    {
        if (r < 0 || r >= n * 3 || c < 0 || c >= n * 3 || visited[r][c] == true || expanded[r][c] == true)
        {
            return;
        }

        visited[r][c] = true;
        dfs(expanded, visited, r + 1, c, n);
        dfs(expanded, visited, r - 1, c, n);
        dfs(expanded, visited, r, c + 1, n);
        dfs(expanded, visited, r, c - 1, n);
    }
};