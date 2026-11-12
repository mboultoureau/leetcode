class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int longuest = 1;
        int decreasing = 1;
        int increasing = 1;

        for (int i = 1; i < nums.size(); ++i) {
            increasing = nums[i - 1] < nums[i] ? increasing + 1 : 1;
            decreasing = nums[i - 1] > nums[i] ? decreasing + 1 : 1;

            longuest = max(longuest, decreasing);
            longuest = max(longuest, increasing);
        }


        return longuest;
    }
};