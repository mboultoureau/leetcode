class Solution {
private:
    vector<vector<string>> result;
    vector<string> grid;

public:
    bool is_valid(int row, int col)
    {
        // Check col
        for (int r = 0; r < row; ++r)
        {
            if (grid[r][col] == 'Q') {
                return false;
            }
        }

        // Check diag NE -> SO
        int r = row - 1;
        int c = col - 1;

        while (r >= 0 && c >= 0)
        {
            if (grid[r][c] == 'Q') {
                return false;
            }

            --r;
            --c;
        }
            
        // Check diag SE --> NO
        r = row - 1;
        c = col + 1;

        while (r >= 0 && c < grid.size())
        {
            if (grid[r][c] == 'Q') {
                return false;
            }

            --r;
            ++c;
        }


        return true;
    }

    vector<vector<string>> solveNQueens(int n) {
        grid.resize(n);
        fill(grid.begin(), grid.end(), string(n, '.'));
    
        backtracking(0);

        return result;
    }

    void backtracking(int row)
    {
        if (row == grid.size())
        {
            result.push_back(grid);
            return;
        }

        for (int col = 0; col < grid.size(); ++col)
        {
            if (is_valid(row, col))
            {
                grid[row][col] = 'Q';
                backtracking(row + 1);
                grid[row][col] = '.';
            }
        }
    }
};