class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int i = 0;
        int n = 0;

        while (i < nums.size())
        {
            // if is the number to replace
            if (nums[i] == n)
            {
                return n;
            }

            // if in the correct place, pass to the next
            if (nums[i] == i + 1)
            {
                i++;
            }
            else
            {
                int next = nums[i];
                nums[i] = n;
                n = next;
                i = max(next - 1, 0);
            }
        }

        return 0;
    }
};