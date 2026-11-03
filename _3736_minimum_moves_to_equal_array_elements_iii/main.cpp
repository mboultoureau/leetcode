class Solution {
public:
    int minMoves(vector<int>& nums) {
        auto it = std::max_element(nums.begin(), nums.end());
        auto maximum = *it;

        int moves = 0;
        for (const int n : nums) {
            moves += abs(n - maximum);
        }
        return moves;
    }
};