class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        struct Cell
        {
            int maximum;
            int nbPaths;
        };
        
        static constexpr int MOD = 1e9 + 7;
        int n = board.size();
        vector<vector<Cell>> grid(n + 1, vector<Cell>(n + 1));
        for (int row = 0; row < n + 1; ++row)
        {
            for (int col = 0; col < n + 1; ++col)
            {
                grid[row][col] = { -1, 0 };
            }
        }

        grid[n - 1][n - 1] = { 0, 1 };
        
        for (int row = n - 1; row >= 0; --row)
        {
            for (int col = n - 1; col >= 0; --col)
            {
                if (board[row][col] == 'X' || board[row][col] == 'S')
                {
                    continue;
                }

                int value = 0;
                if (board[row][col] != 'E')
                {
                    value = board[row][col] - '0';
                }

                std::array<Cell*, 3> neighbors = {&grid[row + 1][col], &grid[row][col + 1], &grid[row + 1][col + 1]};
                int maximum = max({neighbors[0]->maximum, neighbors[1]->maximum, neighbors[2]->maximum});

                if (maximum == -1)
                {
                    grid[row][col] = { -1, 0 };
                    continue;
                }

                int nbPaths = 0;
                for (const auto* cell : neighbors) {
                    if (cell->maximum == maximum) {
                        nbPaths = (nbPaths + cell->nbPaths) % MOD;
                    }
                }

                grid[row][col] = {
                    .maximum = maximum + value,
                    .nbPaths = nbPaths
                };
            }
        }

        if (grid[0][0].maximum == -1)
        {
            return { 0, 0 };
        }

        return { grid[0][0].maximum, grid[0][0].nbPaths };
    }
};