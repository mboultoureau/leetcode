class Solution {
public:
    bool checkString(string s) {
        auto firstB = find(s.begin(), s.end(), 'b');
        auto firstAAfterB = find(firstB, s.end(), 'a');

        return firstAAfterB == s.end();
    }
};