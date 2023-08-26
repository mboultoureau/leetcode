class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int best = 0;

        stack<pair<int, int>> sizes;

        // -->
        sizes.push(make_pair(heights[0], 0));
        for (int i = 1; i < heights.size(); i++) {
            int lastIndex = i;

            while(sizes.size() > 0 && heights[i] < sizes.top().first) {
                best = max(best, sizes.top().first * (i - sizes.top().second));
                lastIndex = sizes.top().second;
                sizes.pop();
            }

            sizes.push(make_pair(heights[i], lastIndex));
        }

        while (sizes.size() > 0) {
            best = max(best, sizes.top().first * ((int) heights.size() - sizes.top().second));
            sizes.pop();
        }

        return best;
    }
};