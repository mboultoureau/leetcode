class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        // 1 <= m, n <= 50
        auto m = grid.size();
        auto n = grid[0].size();

        vector<pair<int, int>> directions {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> distance(m, vector<int>(n, numeric_limits<int>::max()));
        deque<pair<int, int>> queue;

        queue.emplace_front(0, 0);
        distance[0][0] = grid[0][0];
        
        while (!queue.empty())
        {
            const auto [row, col] = queue.front();
            queue.pop_front();

            if (row == m - 1 && col == n - 1)
            {
                return true;
            }

            for (const auto& [directionRow, directionCol] : directions)
            {
                const auto newRow = row + directionRow;
                const auto newCol = col + directionCol;

                // Check if in-bounds
                if (newRow < 0 || newRow >= m || newCol < 0 || newCol >= n)
                {
                    continue;
                }

                const auto total = distance[row][col] + grid[newRow][newCol];
                if (total >= health)
                {
                    continue;
                }

                if (total < distance[newRow][newCol])
                {
                    distance[newRow][newCol] = total;
                    if (grid[newRow][newCol] == 0)
                    {
                        queue.emplace_front(newRow, newCol);
                    }
                    else
                    {
                        queue.emplace_back(newRow, newCol);
                    }
                }
            }
        }

        return false;
    }
};