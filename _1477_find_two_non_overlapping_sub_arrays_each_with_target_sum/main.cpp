class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        vector<int> prefix(n, numeric_limits<int>::max());
        vector<int> suffix(n, numeric_limits<int>::max());      

        // Fill prefix
        int left = 0;
        int sum = 0;
        int best = numeric_limits<int>::max();
        for (int right = 0; right < n; ++right)
        {
            sum += arr[right];

            while (sum > target)
            {
                sum -= arr[left++];
            }

    
            if (sum == target)
            {
                best = min(best, right - left + 1);
            }
    
            prefix[right] = best;
        }

        // Fill suffix
        int right = n - 1;
        sum = 0;
        best = numeric_limits<int>::max();
        for (int left = n - 1; left >= 0; --left)
        {
            sum += arr[left];

            while (sum > target)
            {
                sum -= arr[right--];
            }

            if (sum == target)
            {
                best = min(best, right - left + 1);
            }

            suffix[left] = best;
        }

        // Check
        best = numeric_limits<int>::max();
        for (int i = 0; i < n - 1; ++i)
        {
            if (prefix[i] != numeric_limits<int>::max() && suffix[i + 1] != numeric_limits<int>::max())
            {
                best = min(best, prefix[i] + suffix[i + 1]);
            }

        }

        return best == numeric_limits<int>::max() ? -1 : best;
    }
};