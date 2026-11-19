class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        // Solution 2
        const int n = nums.size();

        if (n <= 3) {
            return 0;
        }

        std::partial_sort(nums.begin(), nums.begin() + 3, nums.end());
        int min0 = nums[0], min1 = nums[1], min2 = nums[2];

        std::partial_sort(nums.begin(), nums.begin() + 3, nums.end(), std::greater<int>());
        int max0 = nums[0], max1 = nums[1], max2 = nums[2];

        return std::min({ max0 - min2, max1 - min1, max2 - min0 });

        // Solution 1
        // const int n = nums.size();

        // if (n <= 3) {
        //     return 0;
        // }

        // std::sort(nums.begin(), nums.end());

        // int result = nums[n - 1] - nums[2];
        // result = min(result, nums[n - 3] - nums[0]);
        // result = min(result, nums[n - 2] - nums[1]);

        // return result;
    }
};