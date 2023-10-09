class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // Solution 2
        int result = nums.size();
        for (int i = 0; i < nums.size(); i++)
        {
            result ^= i ^ nums[i];
        }
        return result;

        // Solution 1
        // sort(nums.begin(), nums.end());

        // for (int i = 0; i < nums.size(); i++)
        // {
        //     if (nums[i] != i)
        //     {
        //         return i;
        //     }
        // }

        // return nums.size();
    }
};