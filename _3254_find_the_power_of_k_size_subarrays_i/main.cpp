class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        vector<int> result;
        int count = 1;

        for (int i = 0; i < nums.size(); i++)
        {
            if (i > 0 && nums[i] == nums[i - 1] + 1)
            {
                count++;
            }
            else
            {
                count = 1;
            }

            if (i + 1 < k)
            {
                continue;
            }

            if (count >= k)
            {
                result.push_back(nums[i]);
            }
            else
            {
                result.push_back(-1);
            }
        }

        return result;
    }
};