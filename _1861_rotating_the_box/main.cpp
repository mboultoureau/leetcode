class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        const int m = boxGrid.size();
        const int n = boxGrid[0].size();

        vector<vector<char>> grid(n, vector<char>(m, '.'));

        for (int r = 0; r < m; ++r) {
            int floor = n - 1;

            for (int c = n - 1; c >= 0; --c) {
                if (boxGrid[r][c] == '*') {
                    grid[c][m - 1 - r] = '*';
                    floor = c - 1;
                } else if (boxGrid[r][c] == '#') {
                    grid[floor][m - 1 - r] = '#';
                    floor--;
                }
            }
        }

        return grid;
    }
};