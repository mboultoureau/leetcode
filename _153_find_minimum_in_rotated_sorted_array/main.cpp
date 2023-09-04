class Solution {
public:
    int findMin(vector<int>& nums) {
        // With NeetCode video solution
        int result = nums[0];
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            if (nums[left] < nums[right]) {
                result = min(result, nums[left]);
                return result;
            }

            int middle = (left + right) / 2;
            result = min(result, nums[middle]);

            if (nums[middle] >= nums[left]) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        return result;
    }
};