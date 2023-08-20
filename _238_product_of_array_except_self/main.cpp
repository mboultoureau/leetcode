class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Same at first attempt but less memory used
        vector<int> result(nums.size());
        result[0] = 1;
        for (int i = 0; i < nums.size() - 1; i++) {
            result[i + 1] = result[i] * nums[i];
        }

        int postfix = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            result[i] = result[i] * postfix;
            postfix = postfix * nums[i];
        }

        return result;

        // Attempt n°1 (with Neetcode solution): take many memory
        // vector<int> prefixes(nums.size());
        // int prefix = 1;
        // for (int i = 0; i < nums.size(); i++) {
        //     prefixes[i] = prefix * nums[i];
        //     prefix = prefixes[i];
        // }

        // vector<int> postfixes(nums.size());
        // int postfix = 1;
        // for (int i = nums.size() - 1; i >= 0; i--) {
        //     postfixes[i] = postfix * nums[i];
        //     postfix = postfixes[i];
        // }

        // vector<int> result(nums.size());
        // result[0] = postfixes[1]; // nums.length >= 2 : OK
        // for (int i = 1; i < nums.size() - 1; i++) {
        //     result[i] = prefixes[i - 1] * postfixes[i + 1];
        // }
        // result[nums.size() - 1] = prefixes[nums.size() - 2];

        // return result;
    }
};