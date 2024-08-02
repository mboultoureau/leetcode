class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Solution 2
        k = k % nums.size();
        std::reverse(nums.begin(), nums.end());
        std::reverse(nums.begin(), nums.begin() + k);
        std::reverse(nums.begin() + k, nums.end());


        // Solution 1
        // Time complexity: O(n)
        // Space complexity: O(1)

        // if (k % nums.size() == 0)
        // {
        //     return;
        // }

        // int loop = std::gcd(k, nums.size());
        // int previous = 0; // Constraint: 1 <= nums.length <= 105
        // int current = 0;
        // for (int offset = 0; offset < loop; offset++)
        // {
        //     previous = nums[(offset - k) % nums.size()];
        //     current = offset;

        //     do
        //     {
        //         int new_previous = nums[current];
        //         nums[current] = previous;
        //         previous = new_previous;
        //         current = (current + k) % nums.size();
        //     } while (current != offset);

        //     nums[current] = previous;
        // }
    }
};