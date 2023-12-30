class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int current = 0;
        int result = 0;

        for (int g : gain) {
            current += g;
            if (current > result) {
                result = current;
            }
        }

        return result;
    }
};