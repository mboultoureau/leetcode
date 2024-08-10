class Solution {
public:
    std::vector<int> shortestDistanceAfterQueries(int n, std::vector<std::vector<int>>& queries) {
        std::vector<int> result(queries.size());
        std::vector<std::vector<int>> roads(n);
        std::vector<int> dp(n);
        
        // Fill dp
        std::iota(dp.begin(), dp.end(), 0);

        for (int i = 0; i < queries.size(); i++)
        {
            roads[queries[i][1]].push_back(queries[i][0]);
            for (int j = queries[i][1]; j < n; j++)
            {
                dp[j] = min(dp[j], dp[j - 1] + 1);
                for (const int dest : roads[j])
                {
                    dp[j] = min(dp[j], dp[dest] + 1);
                }
            }

            result[i] = dp[n - 1];
        }

        return result;
    }
};