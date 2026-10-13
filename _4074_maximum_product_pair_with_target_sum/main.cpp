class Solution {
public:
    vector<int> maxProductPair(vector<int>& nums, int target) {
        vector<int> result{ -1, -1 };
        int best = numeric_limits<int>::min();
        unordered_map<int, int> matchings;
        matchings.reserve(nums.size());

        for (int i = 0; i < nums.size(); ++i) {
            int value = nums[i];
            int remaining = target - value;
            int mult = remaining * value;

            if (value != remaining &&
                matchings.contains(remaining) &&
                mult > best
            ) {
                best = mult;

                if (value > remaining) {
                    result = { i, matchings[remaining] };
                } else {
                    result = { matchings[remaining], i };
                }
            }

            matchings[nums[i]] = i;
        }

        return result;
    }
};