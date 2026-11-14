class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int sum = numeric_limits<int>::max();
        int current = 0;

        for (int i = 0; i < nums.size(); ++i) {
            current = 0;

            for (int j = 0; j < r && j + i < nums.size(); ++j) {
                current += nums[i + j];

                if (j >= l - 1 && j <= r - 1 && current > 0) {
                    sum = min(sum, current);
                }
            }
        }

        return sum == numeric_limits<int>::max() ? -1 : sum;
    }
};