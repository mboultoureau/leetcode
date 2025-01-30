class Solution {
public:
    double myPow(double x, int n) {
        long power = n;
        if (n < 0) {
            return 1.0 / internal_pow(x, -power);
        }

        return internal_pow(x, power);
    }

private:
    double internal_pow(double x, long n) {
        if (n == 0) {
            return 1.0;
        }

        if (n % 2 == 0) {
            return myPow(x * x, n / 2);
        } else {
            return x * myPow(x * x, (n - 1) / 2);
        }
    }
};