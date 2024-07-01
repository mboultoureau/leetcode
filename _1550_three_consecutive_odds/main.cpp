class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        unsigned char numberOfOdds = 0;
        for (const int& number : arr) {
            if (number % 2 == 0) {
                numberOfOdds = 0;
                continue;
            }

            numberOfOdds += 1;
            if (numberOfOdds == 3) {
                return true;
            }
        }

        return false;
    }
};