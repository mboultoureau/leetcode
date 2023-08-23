class Solution {
public:
    int trap(vector<int>& height) {
        // THIRD ATTEMPT (with NeetCode video)
        int left = 0;
        int right = height.size() - 1;
        int maxLeft = height[left];
        int maxRight = height[right];
        int area = 0;

        while (left < right) {
            if (maxLeft <= maxRight) {
                left += 1;
                maxLeft = max(maxLeft, height[left]);
                area += maxLeft - height[left];
            } else {
                right -= 1;
                maxRight = max(maxRight, height[right]);
                area += maxRight - height[right];
            }
        }

        return area;

        // SECOND ATTEMPT (with NeetCode video) : Work but many memory used
        // vector<int> maxLeft(height.size());
        // vector<int> maxRight(height.size());
        // vector<int> minimum(height.size());

        // maxLeft[0] = 0;
        // for (int i = 1; i < height.size(); i++) {
        //     maxLeft[i] = max(height[i - 1], maxLeft[i - 1]);
        // }

        // maxRight[height.size() - 1] = 0;
        // for (int i = height.size() - 2; i >= 0; i--) {
        //     maxRight[i] = max(height[i + 1], maxRight[i + 1]);
        // }

        // for (int i = 0; i < height.size(); i++) {
        //     minimum[i] = min(maxLeft[i], maxRight[i]);
        // }

        // int area = 0;
        // for (int i = 0; i < height.size(); i++) {
        //     area += max(minimum[i] - height[i], 0);
        // }

        // return area;



        // FIRST ATTEMPT: Work but too slow, Time Limit Exceeded in 321/322th:(
        // int area = 0;
        // int left = 0;
        // int right = height.size() - 1;
        // int maxHeight = 0;

        // // Find first wall on each side
        // while (left < right && height[left] == 0) {
        //     left++;
        // }

        // while (left < right && height[right] == 0) {
        //     right--;
        // }

        // // Main logic (like 11. Container With Most Water)
        // while (left < right) {
        //     // if the height > left or right, we have already covered this case
        //     if (height[left] < maxHeight) {
        //         left++;
        //         continue;
        //     }

        //     if (height[right] < maxHeight) {
        //         right--;
        //         continue;
        //     }

        //     int wallHeight = min(height[left], height[right]);

        //     // Calculate area
        //     for (int i = left + 1; i < right; i++) {
        //         if (height[i] < wallHeight) {
        //             area += wallHeight - max(maxHeight, height[i]);
        //         }
        //     }

        //     maxHeight = wallHeight;

        //     if (height[left] > height[right]) {
        //         right--;
        //     } else {
        //         left++;
        //     }

        // }

        // return area;
    }
};