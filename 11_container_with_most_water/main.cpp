class Solution {
public:
    int maxArea(vector<int>& height) {
        // SECOND ATTEMPT (with NeetCode video)
        int maxArea = 0;
        int left = 0;
        int right = height.size() - 1;

        while (left < right) {
            int a = (right - left) * min(height[left], height[right]);
            maxArea = max(a, maxArea);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;

        // FIRST ATTEMPT O(n²) --> too slow for some tests
        // int maxArea = 0;

        // for (int i = 0; i < height.size() - 1; i++) {
        //     for (int j = i + 1; j < height.size(); j++) {
        //         int a = (j - i) * min(height[i], height[j]);
        //         if (a > maxArea) {
        //             maxArea = a;
        //         }
        //     }
        // }

        // return maxArea;
    }
};