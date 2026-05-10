class Solution {
public:
    int maximumJumps(vector<int>& nums, int target) {
        size_t n = nums.size();
        vector<int> cache(n, std::numeric_limits<int>::min());
        cache[0] = 0;

        for (int i = 1; i < n; ++i)
        {
            if (cache[i] == -1)
            {
                continue;
            }

            for (int j = 0; j < i; ++j)
            {
                if (abs(nums[j] - nums[i]) <= target)
                {
                    cache[i] = max(cache[i], 1 + cache[j]);
                }
            }
        }

        return cache[n - 1] < 0 ? -1 : cache[n - 1];
    }
};