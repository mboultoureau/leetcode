class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        // Optimized approch
        vector<int> result;

        for (int i = nums.size() - 1; i >= 0; --i)
        {
            int n = nums[i];
            while (n > 0)
            {
                result.push_back(n % 10);
                n /= 10;
            }
        }
        
        std::reverse(std::begin(result), std::end(result));
        return result;
        
        
        // // Naive approch
        // vector<int> result;

        // for (const auto& n : nums)
        // {
        //     const auto str = std::to_string(n);
        //     for (char c : str)
        //     {
        //         result.push_back(c - '0');
        //     }
        // }

        // return result;
    }
};