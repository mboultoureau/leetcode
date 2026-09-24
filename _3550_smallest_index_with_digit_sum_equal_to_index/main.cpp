class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i)
        {
            int current = nums[i];
            int sum = 0;

            while (current != 0)
            {
                sum += current % 10;
                current /= 10;
            }

            if (sum == i) 
            {
                return i;
            }
        }

        return -1;
    }
};