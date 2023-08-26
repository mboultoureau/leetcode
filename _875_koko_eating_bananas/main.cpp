class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());
        int k = right;

        while (left <= right) {
            int middle = (left + right) / 2;

            // Calculate time
            long time = 0;
            for (int i = 0; i < piles.size(); i++) {
                time += max((piles[i] + (middle - 1)) / middle, 1);
            }

            if (time > h) {
                left = middle + 1;
            } else {
                k = middle;
                right = middle - 1;
            }
        }

        return k;
    }
};