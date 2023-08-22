class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // With NeetCode video help
        vector<vector<int>> result;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 2; i++) {
            // Optimization because sorted
            if (nums[i] > 0) break;

            // Skip to avoid duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.push_back({ nums[i], nums[left], nums[right] });

                    // Result found, but many other results can occurs (but not with same numbers because no duplicates)
                    // Careful, needs to avoid duplicates
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    left++;

                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    right--;
                } else if (sum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }

        return result;
    }
};