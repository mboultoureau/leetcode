class Solution {
public:
    int minAddToMakeValid(string s) {
        int result = 0;
        int count = 0;

        for (const char c : s) {
            if (c == '(') {
                count++;
            } else {
                count--;
            }

            if (count < 0) {
                result += -count;
                count = 0;
            }
        }

        result += count;

        return result;
    }
};