class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        const size_t m = grid.size();
        const size_t n = grid[0].size();
        const int K = 1024;

        vector<bitset<K>> xorGrid(n);

        for (size_t r = 0; r < m; ++r) {
            for (size_t c = 0; c < n; ++c) {
                const int g = grid[r][c];
                bitset<K> next;

                if (r == 0 && c == 0) {
                    next[g] = true;
                } else {
                    for (int v = 0; v < K; ++v) {
                        const bool fromUp   = r > 0 && xorGrid[c][v];
                        const bool fromLeft = c > 0 && xorGrid[c - 1][v];
                        if (fromUp || fromLeft) {
                            next[v ^ g] = true;
                        }
                    }
                }
                xorGrid[c] = next;
            }
        }

        for (int v = 0; v < K; ++v) {
            if (xorGrid[n - 1][v]) {
                return v;
            } 
        }

        return -1;


        // // Solution 2
        // vector<vector<unordered_set<int>>> xorGrid;
        // const size_t m = grid.size();
        // const size_t n = grid[0].size();

        // // First row
        // xorGrid.push_back({ { grid[0][0] } });
        // for (size_t c = 1; c < n; ++c) {
        //     xorGrid[0].push_back({ *(xorGrid[0][c - 1].begin()) ^ grid[0][c] });
        // }

        // // First col
        // for (size_t r = 1; r < m; ++r) {
        //     xorGrid.push_back({ { *(xorGrid[r - 1][0].begin()) ^ grid[r][0] } });
        // }

        // // End
        // for (size_t r = 1; r < m; ++r) {
        //     for (size_t c = 1; c < n; ++c) {
        //         xorGrid[r].push_back({});

        //         for (const int value : xorGrid[r - 1][c]) {
        //             xorGrid[r][c].insert(value ^ grid[r][c]);
        //         }
            
        //         for (const int value : xorGrid[r][c - 1]) {
        //             xorGrid[r][c].insert(value ^ grid[r][c]);
        //         }
        //     }
        // }

        // int minimum = numeric_limits<int>::max();
        // for (const int value : xorGrid[m - 1][n - 1]) {
        //     minimum = min(minimum, value);
        // }

        // return minimum;
    }
};