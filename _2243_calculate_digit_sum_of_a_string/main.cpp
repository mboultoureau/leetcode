class Solution {
public:
    string digitSum(string s, int k) {
        string new_string;

        while (s.size() > k)
        {
            new_string = "";

            for (int i = 0; i < s.size(); i += k) {
                int sum = 0;

                for (int j = 0; j < k && i + j < s.size(); ++j) {
                    sum += (s[i + j] - '0');
                }

                new_string += to_string(sum);
            }

            s = new_string;
        }

        return s;
    }
};