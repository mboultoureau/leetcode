class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int target = accumulate(nums.begin(), nums.end(), 0) - x;
        int current = 0;
        int best = -1;

        int left = 0;
        int right = 0;

        while (right < nums.size()) {
            current += nums[right];

            while (current > target && left < nums.size()) {
                current -= nums[left];
                left++;
            }

            if (current == target)
            {
                best = max(best, right - left + 1);
            }

            right++;
        }

        return best == - 1 ? -1 : nums.size() - best;
    }
};