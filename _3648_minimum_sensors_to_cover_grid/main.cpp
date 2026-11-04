class Solution {
public:
    int minSensors(int n, int m, int k) {
        int side = 1 + k * 2;
        int a = ceil(n / static_cast<double>(side));
        int b = ceil(m / static_cast<double>(side));

        return a * b;
    }
};