class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int count = 0;
        int nb_rows = grid.size();
        int nb_cols = grid[0].size();

        for (int row = 0; row < nb_rows - 2; row++)
        {
            for (int col = 0; col < nb_cols - 2; col++)
            {
                int sum = grid[row][col] + grid[row][col + 1] + grid[row][col + 2];

                if (!checkDistincts(grid, row, col) || 
                    !checkRows(grid, row, col, sum) ||
                    !checkCols(grid, row, col, sum) ||
                    !checkDiagonals(grid, row, col, sum))
                {
                    continue;
                }
                
                count += 1;
            }
        }

        return count;
    }

    bool checkDiagonals(vector<vector<int>>& grid, int row, int col, int sum)
    {
        if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != sum)
        {
            return false;
        }

        if (grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != sum)
        {
            return false;
        }

        return true;
    }

    bool checkRows(vector<vector<int>>& grid, int row, int col, int sum)
    {
        for (int i = 0; i < 3; i++)
        {
            int rowSum = grid[row + i][col] + grid[row + i][col + 1] + grid[row + i][col + 2];
            if (rowSum != sum)
            {
                return false;
            }
        }
        return true;
    }

    bool checkCols(vector<vector<int>>& grid, int row, int col, int sum)
    {
        for (int i = 0; i < 3; i++)
        {
            int colSum = grid[row][col + i] + grid[row + 1][col + i] + grid[row + 2][col + i];
            if (colSum != sum)
            {
                return false;
            }
        }
        return true;
    }

    bool checkDistincts(vector<vector<int>>& grid, int row, int col)
    {
        std::array<int, 9> numbers = {0};
        for (int i = 0; i < 9; i++)
        {
            int r = row + (i / 3);
            int c = col + (i % 3);

            if (grid[r][c] < 1 || grid[r][c] > 9)
            {
                return false;
            }

            numbers[grid[r][c] - 1] += 1;
            if (numbers[grid[r][c] - 1] != 1)
            {
                return false;
            }
        }

        return true;
    }
};