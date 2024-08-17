class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        // Time complexity : O(m x n)
        // Space complexity: O(n)
        int m = points.size();
        int n = points[0].size();

        vector<long long> previous(n);
        vector<long long> left(n);
        vector<long long> right(n);
        vector<long long> current(n);

        for (int c = 0; c < n; c++)
        {
            previous[c] = points[0][c];
        }

        left[0] = points[0][0];
        for (int c = 1; c < n; c++)
        {
            left[c] = max((long long)points[0][c], left[c - 1] - 1);
        }

        right[n - 1] = points[0][n - 1];
        for (int c = n - 2; c >= 0; c--)
        {
            right[c] = max((long long)points[0][c], right[c + 1] - 1);
        }

        for (int r = 1; r < m; r++)
        {
            for (int c = 0; c < n; c++)
            {
                current[c] = (long long)points[r][c] + max(left[c], right[c]);
            }

            for (int c = 0; c < n; c++)
            {
                previous[c] = current[c];
            }

            left[0] = current[0];
            for (int c = 1; c < n; c++)
            {
                left[c] = max((long long)current[c], left[c - 1] - 1);
            }

            right[n - 1] = current[n - 1];
            for (int c = n - 2; c >= 0; c--)
            {
                right[c] = max((long long)current[c], right[c + 1] - 1);
            }
        }

        long long result = INT_MIN;
        for (const long long& n : previous)
        {
            result = max(result, n);
        }

        return result;


        // Time Limit Exceeded
        // Time complexity: O(m x n x n)
        // Space complexity: O(n)

        // int m = points.size();
        // int n = points[0].size();

        // vector<long long> previous(n);
        // vector<long long> current(n);

        // for (int c = 0; c < n; c++)
        // {
        //     previous[c] = points[0][c];
        // }

        // for (int r = 1; r < m; r++)
        // {
        //     for (int c = 0; c < n; c++)
        //     {
        //         current[c] = LLONG_MIN;
        //         for (int pc = 0; pc < n; pc++)
        //         {
        //             current[c] = max(current[c], points[r][c] + previous[pc] - abs(c - pc));
        //         }
        //     }

        //     for (int c = 0; c < n; c++)
        //     {
        //         previous[c] = current[c];
        //     }
        // }

        // long long result = INT_MIN;
        // for (const long long& n : previous)
        // {
        //     result = max(result, n);
        // }

        // return result;
    }
};