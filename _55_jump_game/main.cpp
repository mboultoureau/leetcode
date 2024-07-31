class Solution {
public:
    bool canJump(vector<int>& nums) {
        // Solution 2
        int maximum = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (i > maximum)
            {
                return false;
            }

            maximum = max(maximum, i + nums[i]);
            if (maximum >= nums.size() - 1)
            {
                return true;
            }
        }

        return true;

        // Solution 1
        // int goal = nums.size() - 1;
        // for (int i = nums.size() - 1; i >= 0; i--)
        // {
        //     if (i + nums[i] >= goal)
        //     {
        //         goal = i;
        //     }
        // }

        // return goal == 0;
    }
};