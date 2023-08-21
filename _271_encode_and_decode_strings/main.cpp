class Solution {
public:
    /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    string encode(vector<string> &strs) {
        // write your code here
        string result = "";
        for (int i = 0; i < strs.size(); i++) {
            result += to_string(strs[i].size()) + ":" + strs[i];
        }
        cout << result;
        return result;
    }

    /*
     * @param str: A string
     * @return: decodes a single string to a list of strings
     */
    vector<string> decode(string &str) {
        vector<string> result;
        int i = 0;
        string length = "";

        while (i < str.size()) {
            if (str[i] == ':') {
                int nb = stoi(length);
                result.push_back(str.substr(i + 1, nb));
                i += nb + 1;
                length = "";
            }

            length += str[i];

            i++;
        }

        return result;
    }
};

// Done on Lintcode: https://www.lintcode.com/problem/659/solution