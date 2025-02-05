class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        // Constraint : s1.length == s2.length, don't check length
        int firstDiff = 0;
        int secondDiff = 0;
        int nbDiffs = 0;

        for (int i = 0; i < s1.size(); i++) {
            if (s1[i] == s2[i]) {
                continue;
            }

            if (nbDiffs == 0) {
                firstDiff = i;
            } else if (nbDiffs == 1) {
                secondDiff = i;
            } else {
                return false;
            }

            nbDiffs++;
        }

        return s1[firstDiff] == s2[secondDiff] && s1[secondDiff] == s2[firstDiff];
    }
};