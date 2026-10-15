class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int sum = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
            std::unordered_set<int> numbers;

            for (int j = i; j < nums.size(); ++j)
            {
                numbers.insert(nums[j]);
                sum += numbers.size() * numbers.size();
            }
        }

        return sum;
    }
};