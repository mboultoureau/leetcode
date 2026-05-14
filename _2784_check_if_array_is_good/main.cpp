class Solution {
public:
    bool isGood(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (size_t i = 0; i < nums.size() - 1; ++i)
        {
            if (i + 1 != nums[i])
            {
                return false;
            }
        }

        return nums[nums.size() - 1] == nums.size() - 1;
    }
};