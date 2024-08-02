class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int maximum = 0;
        int count = 0;
        int current = 0;

        // Count the number of 1
        for (const int& n : nums)
        {
            if (n == 1)
            {
                count++;
            }
        }

        // Find the sliding window of size count with the maximum number of 1
        for (int i = 0; i < count; i++)
        {
            current += nums[i];
        }

        for (int i = 0; i < nums.size(); i++)
        {
            maximum = std::max(maximum, current);
            current -= nums[i];
            current += nums[(i + count) % nums.size()];
        }

        return count - maximum;
    }
};