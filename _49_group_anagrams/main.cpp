class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // With solution watched (Neetcode)
        // unordered_map<string, vector<string>> anagrams;

        // for (int i = 0; i < strs.size(); i++) {
        //     vector<int> count(26);

        //     for (int c = 0; c < strs[i].size(); c++) {
        //         count[strs[i][c] - 'a'] += 1;
        //     }

        //     string key = "";
        //     for (int j = 0; j < count.size(); j++) {
        //         key.append(to_string(count[j]) + '-');
        //     }

        //     // Exemple: bat -> 1-1-0-....-0-1-0-0-...- (1 for a, 1 for b, 0 for c, ...)

        //     anagrams[key].push_back(strs[i]);
        // }

        // vector<vector<string>> result;
        // for (auto it : anagrams) {
        //     result.push_back(it.second);
        // }

        // return result;

        // First attempt: good but sorted is too long
        unordered_map<string, vector<string>> anagrams;

        for (int i = 0; i < strs.size(); i++) {
            string sorted = strs[i];
            sort(sorted.begin(), sorted.end());
            anagrams[sorted].push_back(strs[i]);
        }

        vector<vector<string>> result;
        for (auto it : anagrams) {
            result.push_back(it.second);
        }

        return result;
    }
};