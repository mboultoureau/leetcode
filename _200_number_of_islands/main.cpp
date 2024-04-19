class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int result = 0;

        for (int y = 0; y < grid.size(); y++) {
            for (int x = 0; x < grid[0].size(); x++) {
                if (grid[y][x] == '1') {
                    result += 1;
                    dfs(grid, y, x);
                }
            }
        }

        return result;
        
    }

    void dfs(vector<vector<char>>& grid, int y, int x) {
        if (y < 0 || y >= grid.size() || x < 0 || x >= grid[0].size() || grid[y][x] != '1') {
            return;
        }

        grid[y][x] = '0';

        dfs(grid, y - 1, x);
        dfs(grid, y + 1, x);
        dfs(grid, y, x - 1);
        dfs(grid, y, x + 1);
    }

    
};