class Solution {
public:
    long long sumAndMultiply(int n) {
        long long x = 0;
        long long sum = 0;
        long long exposant = 1;

        while (n != 0)
        {
            int digit = n % 10;
            sum += digit;

            if (digit != 0)
            {
                x += digit * exposant;
                exposant *= 10;
            }

            n /= 10;
        }

        x *= sum;

        return x;
    }
};