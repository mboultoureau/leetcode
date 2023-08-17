class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> runningSum(nums.size()); // allocate memory take much time, but less memory
        runningSum[0] = nums[0];

        for (unsigned int i = 1; i < nums.size(); i++) {
            runningSum[i] = runningSum[i - 1] + nums[i];
        }

        return runningSum;


        // Faster way: don't create a new array but instead modify the previous one (used `nums` array)
    }
};