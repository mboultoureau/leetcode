class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        // Approch 2: no sort (looking at solution)
        int n = arr.size();
        vector<int> freq = vector(n + 1, 0);

        for (int i : arr)
        {
            freq[std::min(i, n)] += 1;
        }

        auto current = 1;
        for (auto i = 2; i <= n; ++i)
        {
            current = min(current + freq[i], i);
        }

        return current;

        // Approch 1: sort
        // std::sort(arr.begin(), arr.end());
        
        // auto current = 1;
        // for (auto i = 1; i < arr.size(); ++i)
        // {
        //     current = std::min(current + 1, arr[i]);
        // }

        // return current;
    }
};