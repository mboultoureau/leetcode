class Solution {
public:
    int findKOr(vector<int>& nums, int k) {
        int total = 0;
        int result = 0;

        for (int i = 0; i < 32; i++) {
            total = 0;
            for (const int &n : nums) {
                total += (n >> i) & 1;
            }

            if (total >= k) {
                result |= (1 << i);
            }
        }

        return result;
    }
};