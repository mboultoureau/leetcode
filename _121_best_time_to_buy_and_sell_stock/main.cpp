class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // With Neetcode video solution
        int left = 0;
        int right = 1;
        int maxProfit = 0;

        while (right < prices.size()) {
            if (prices[left] >= prices[right]) {
                left = right;
            } else {
                maxProfit = max(maxProfit, prices[right] - prices[left]);
            }

            right++;
        }

        return maxProfit;
    }
};