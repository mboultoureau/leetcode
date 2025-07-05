class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int, int> numbers;
        int result = -1;

        for (int n : arr)
        {
            numbers[n]++;
        }

        for (auto& [n, freq] : numbers)
        {
            if (n == freq)
            {
                result = max(result, n);
            }
        }

        return result;
    }
};