class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        // Solution 2
        if (sum > 9 * num) {
            return "";
        }

        string result(num, '0');

        int nines = sum / 9;
        int remainder = sum % 9;

        fill_n(result.begin(), nines, '9');
        result[nines] = '0' + remainder;

        return result;

        // // Solution 1
        // if (sum > 9 * num) {
        //     return "";
        // }

        // string result;
        // result.reserve(num);

        // for (int i = 0; i < num; ++i)
        // {
        //     int digit = min(sum, 9);
        //     sum -= digit;
        //     result += to_string(digit);
        // }        

        // return result;
    }
};