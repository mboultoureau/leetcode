class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_map<int, int> count;
        for (int n : nums)
        {
            count[n] += 1;
            if (count[n] > 1)
            {
                return n;
            }
        }

        return 0;
    }
};