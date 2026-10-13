class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b) {
            return abs(a) < abs(b);
        });

        long long result = 0;
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            result += nums[right] * nums[right];
            result -= nums[left] * nums[left];
            left++;
            right--;
        }

        if (left == right) {
            result += nums[right] * nums[right];
        }

        return result;
    }
};