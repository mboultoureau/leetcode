class Solution {
public:
    int semiOrderedPermutation(vector<int>& nums) {
        int first = -1;
        int last = -1;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                first = i;
            } else if (nums[i] == nums.size()) {
                last = i;
            }
        }

        if (first < last) {
            return first + nums.size() - last - 1;
        } else {
            return first + nums.size() - last - 2;
        }
    }
};