class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        // Solution 3
        // std::sort(nums.begin(), nums.end());

        // vector<int> dp(nums.back() + 2);
        // int maximum = 1;

        // for (auto& n : nums) {
        //     dp[n + 1] = max(dp[n + 1], dp[n] + 1);
        //     dp[n] = max(dp[n], dp[n - 1] + 1);
        //     maximum = max({ maximum, dp[n], dp[n + 1] });
        // }

        // return maximum;


        // Solution 2
        std::sort(nums.begin(), nums.end());

        array<int, 3> dp{};
        int maximum = 1;
        int previous = nums[0];

        for (auto& n : nums) {
            int diff = n - previous;

            if (diff == 1) dp = { dp[1], dp[2], 0 };
            else if (diff == 2) dp = { dp[2], 0, 0 };
            else if (diff >= 3) dp = { 0, 0, 0 };
            previous = n;

            dp[2] = max(dp[2], dp[1] + 1);
            dp[1] = max(dp[1], dp[0] + 1);
            maximum = max({ maximum, dp[1], dp[2] });
        }

        return maximum;


        // Solution 1
        // std::sort(nums.begin(), nums.end());

        // unordered_map<int, int> dp;
        // int maximum = 1;

        // for (auto& n : nums) {
        //     dp[n + 1] = max(dp[n + 1], dp[n] + 1);
        //     dp[n] = max(dp[n], dp[n - 1] + 1);
        //     maximum = max({ maximum, dp[n], dp[n + 1] });
        // }

        // return maximum;
    }
};