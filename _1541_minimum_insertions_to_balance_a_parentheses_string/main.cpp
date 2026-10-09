class Solution {
public:
    int minInsertions(string s) {
        int parentheses{ 0 }, insertions{ 0 };

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                parentheses++;
                continue;
            }

            if (parentheses > 0) {
                parentheses--;
            } else {
                insertions += 1;
            }

            if (i + 1 == s.size() || s[i + 1] != ')') {
                insertions++;
            } else {
                i++;
            }
        }

        return insertions + parentheses * 2;
    }
};