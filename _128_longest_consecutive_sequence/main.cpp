class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // cannot be sorted because constraint O(n) time

        // Solution (with Neetcode video)
        unordered_set<int> numsSet(nums.begin(), nums.end());
        int maxLength = 0;

        for (int i = 0; i < nums.size(); i++) {
            // if there is are a left number, skip
            if (numsSet.find(nums[i] - 1) != numsSet.end()) {
                continue;
            }

            // if first of sequence, calculate length
            int length = 1;
            while (numsSet.find(nums[i] + length) != numsSet.end()) {
                length += 1;
            }

            if (length > maxLength) {
                maxLength = length;
            }
        }

        return maxLength;
    }
};