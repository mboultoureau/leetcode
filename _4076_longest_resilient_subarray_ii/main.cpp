class Solution {
public:
    int resilientSubarray(vector<int>& nums, int k) {
        const int n = nums.size();
        int longuest = 1;

        int left = 0;
        int right = 0;
        int sum = 0;
        
        while (right < n)
        {
            if (nums[left] % k == nums[right] % k) {
                sum = ((nums[right] % k) + sum) % k;
                
                if (sum % k == nums[right] % k) {
                    longuest = max(longuest, right - left + 1);
                }
 
                right++;
            } else {
                sum = 0;
                left = right;
            }

        }

        return longuest;
    }
};