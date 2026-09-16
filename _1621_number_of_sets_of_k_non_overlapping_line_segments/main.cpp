class Solution {
public:
    int numberOfSets(int n, int k) {
        int nbCols = n;
        int nbRows = k + 1;
        const int mod = 1'000'000'000 + 7;

        vector<vector<int>> dp(nbRows, vector<int>(nbCols));

        int last = 0;

        // Fill last line with [n, 0]
        for (int col = 0; col < nbCols; ++col)
        {
            dp[k][col] = n - col;
        }

        for (int row = nbRows - 2; row >= 0; --row)
        {
            last = 0;
            for (int col = nbCols - (k - row + 1); col >= 0; --col)
            {
                int current = (last + dp[row + 1][col + 1]) % mod;
                dp[row][col] = (current + dp[row][col + 1]) % mod;
                last = current;
            }
        }

        return last;
    }
};