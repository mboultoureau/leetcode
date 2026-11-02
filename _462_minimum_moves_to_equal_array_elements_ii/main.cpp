class Solution {
public:
    int minMoves2(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int midIdx = nums.size() / 2;
        int mid = nums[midIdx];

        int moves = 0;
        for (const int n : nums) {
            moves += abs(mid - n);
        }
        return moves;
    }
};