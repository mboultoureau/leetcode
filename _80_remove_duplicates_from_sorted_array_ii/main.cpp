class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // SECOND ATTEMPT (with Solution)
        int i = 0;
        for (int n : nums) {
            if (i < 2 || n > nums[i - 2]) {
                nums[i] = n;
                i++;
            }
        }

        return i;

        // FIRST ATTEMPT
        // int repetitions = 1;
        // int previous = nums[0];
        // int j = 1;

        // for (int i = 1; i < nums.size(); i++) {
        //     if (previous == nums[i]) {
        //         repetitions++;
        //     } else {
        //         repetitions = 1;
        //     }

        //     if (repetitions <= 2) {
        //         nums[j] = nums[i];
        //         j++;
        //     }

        //     previous = nums[i];
        // }

        // return j;
    }
};