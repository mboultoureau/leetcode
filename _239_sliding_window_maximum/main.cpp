class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int left = 1;
        int right = k;

        deque<int> dq;
        vector<int> result;

        for (int i = 0; i < k; i++)
        {
            while (!dq.empty() && nums[dq.back()] <= nums[i])
            {
                dq.pop_back();
            }
            dq.push_back(i);
        }
        result.push_back(nums[dq.front()]);

        while (right < nums.size())
        {
            while (!dq.empty() && nums[dq.back()] < nums[right])
            {
                dq.pop_back();
            }
            dq.push_back(right);

            if (left > dq.front())
            {
                dq.pop_front();
            }

            result.push_back(nums[dq.front()]);

            left++;
            right++;
        }

        return result;


        // Good memory but slow
        // int left = 0;
        // int right = k - 1;

        // int max = nums[0];
        // int idx = -1;

        // vector<int> result(nums.size() - k + 1);

        // while (right < nums.size())
        // {
        //     if (idx >= left)
        //     {
        //         if (nums[right] >= max)
        //         {
        //             max = nums[right];
        //             idx = right;
        //         }
        //     }
        //     // Recalculate max
        //     else
        //     {
        //         max = nums[left];
        //         idx = left;
        //         for (int i = left + 1; i <= right; i++)
        //         {
        //             if (nums[i] >= max)
        //             {
        //                 max = nums[i];
        //                 idx = i;
        //             }
        //         }
        //     }

        //     result[left] = max;

        //     left++;
        //     right++;
        // }

        // return result;
    }
};