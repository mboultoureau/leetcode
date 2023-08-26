class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        if (str2.size() > str1.size()) {
            return false;
        }

        int j = 0;
        for (int i = 0; i < str1.size() && j < str2.size(); i++) {
            if (str2[j] == str1[i] || (str2[j] == (str1[i] - 'a' + 1) % 26 + 'a')) {
                j++;
            } 
        }

        return j == str2.size();
    }
};