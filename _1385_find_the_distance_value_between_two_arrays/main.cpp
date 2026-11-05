class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        int result = arr1.size();

        for (const int a : arr1) {
            for(const int b : arr2) {
                if (abs(a - b) <= d) {
                    result--;
                    break;
                }
            }
        }

        return result;
    }
};