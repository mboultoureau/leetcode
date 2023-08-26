class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size());
        result[temperatures.size() - 1] = 0;

        for (int i = temperatures.size() - 2; i >= 0; i--) {
            result[i] = 1;
            int j = i + 1;

            while (temperatures[j] <= temperatures[i]) {
                if (result[j] == 0) {
                    result[i] = 0;
                    break;
                }

                result[i] += result[j];
                j += result[j];
            }
        }

        return result;
    }
};