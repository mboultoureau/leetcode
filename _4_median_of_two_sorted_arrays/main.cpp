class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // If merge, time complexity is exceeded

        // Edges cases: nums1 or nums2 is empty
        // they can't be empty in the same time (from description)

        // Not necessary but faster on LeetCode
        // if (nums1.size() == 0)
        // {
        //     if (nums2.size() % 2 == 0)
        //     {
        //         return (nums2[nums2.size() / 2 - 1] + nums2[nums2.size() / 2]) / 2.0;
        //     }
        //     else
        //     {
        //         return nums2[nums2.size() / 2];
        //     }
        // }

        // if (nums2.size() == 0)
        // {
        //     if (nums1.size() % 2 == 0)
        //     {
        //         return (nums1[nums1.size() / 2 - 1] + nums1[nums1.size() / 2]) / 2.0;
        //     }
        //     else
        //     {
        //         return nums1[nums1.size() / 2];
        //     }
        // }

        // With NeetCode video solution
        if (nums1.size() > nums2.size())
        {
            return findMedianSortedArrays(nums2, nums1);
        }

        int total = nums1.size() + nums2.size();
        int left = 0;
        int right = nums1.size();

        while (left <= right)
        {
            int middleNums1 = left + (right - left) / 2;
            int middleNums2 = (total + 1) / 2 - middleNums1;

            int leftNums1 = INT_MIN;
            if (middleNums1 > 0)
            {
                leftNums1 = nums1[middleNums1 - 1];
            }

            int rightNums1 = INT_MAX;
            if (middleNums1 < nums1.size())
            {
                rightNums1 = nums1[middleNums1];
            }

            int leftNums2 = INT_MIN;
            if (middleNums2 > 0)
            {
                leftNums2 = nums2[middleNums2 - 1];
            }

            int rightNums2 = INT_MAX;
            if (middleNums2 < nums2.size())
            {
                rightNums2 = nums2[middleNums2];
            }

            if (leftNums1 <= rightNums2 && leftNums2 <= rightNums1)
            {
                if (total % 2 == 0)
                {
                    return (max(leftNums1, leftNums2) +  min(rightNums1, rightNums2)) / 2.0;
                }
                else
                {
                    return max(leftNums1, leftNums2);
                }
            }
            else if (leftNums1 > leftNums2)
            {
                right = middleNums1 - 1;
            }
            else
            {
                left = middleNums1 + 1;
            }
        }

        return 0.0;
    }
};