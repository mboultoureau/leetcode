class Solution {
public:
    bool isAnagram(string s, string t) {
        // Solution 1
        if (s.size() != t.size()) {
            return false;
        }

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        if (s.compare(t) == 0) {
            return true;
        }

        return false;

        // Solution 2
        // if (s.size() != t.size()) {
        //     return false;
        // }

        // array<int, 26> container{};
        // for (const auto c : s) {
        //     container[c - 'a']++;
        // }

        // for (const auto c : t) {
        //     if (container[c - 'a'] == 0) {
        //         return false;
        //     }

        //     container[c - 'a']--;
        // }


        // return true;



        // Solution 3
        // if (s.size() != t.size()) {
        //     return false;
        // }

        // unordered_map<char, int> container;
        // for (const auto c : s) {
        //     container[c]++;
        // }

        // for (const auto c : t) {
        //     if (container[c] == 0) {
        //         return false;
        //     }

        //     container[c]--;
        // }


        // return true;
    }
};