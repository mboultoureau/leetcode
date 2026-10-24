class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int sum = accumulate(rolls.begin(), rolls.end(), 0);

        int total = mean * (n + m) - sum;
        if (total < n || total > 6 * n) {
            return {};
        }

        int dice = total / n;
        int remaining = total % n;

        vector<int> result(n, dice);

        for (int i = 0; i < remaining; ++i) {
            result[i]++;
        }

        return result;

 




        // int m = rolls.size();
        // int sum = accumulate(rolls.begin(), rolls.end(), 0);
        // int low = n;
        // int high = n * 6;
        // double epsilon = 1e-9;

        // while (low <= high)
        // {
        //     int mid = (low + high) / 2;
        //     double current_mean = (sum + mid) / (static_cast<double>(m) + static_cast<double>(n));

        //     if (abs(current_mean - mean) < epsilon) {
        //         int dice = mid / n;
        //         int remaining = mid % n;

        //         cout << dice << " " << remaining << endl;

        //         vector<int> result(n, dice);

        //         int i = 0;
        //         while (remaining != 0) {
        //             int increment = min(6 - result[i], remaining);
        //             result[i] += increment;
        //             remaining -= increment;
        //             ++i;
        //         }

        //         return result;

        //     } else if (current_mean < mean) {
        //         low = mid + 1;
        //     } else {
        //         high = mid - 1;
        //     }
        // }

        // return {};
    }
};