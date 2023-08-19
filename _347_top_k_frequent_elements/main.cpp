class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Solution (Neetcode) : Bucket sort
        // Step 1: count all nums frequency
        unordered_map<int, int> count_map;
        for (int i = 0; i < nums.size(); i++) {
            count_map[nums[i]] += 1;
        }

        // Create a n array with count as key, nums as values
        vector<vector<int>> frequencies(nums.size() + 1);
        for (auto i : count_map) {
            frequencies[i.second].push_back(i.first);
        }

        // Get k most frequent elements
        vector<int> result;
        for (int i = frequencies.size() - 1; i >= 0; i--) {
            for (int j = 0; j < frequencies[i].size(); j++) {
                result.push_back(frequencies[i][j]);

                if (result.size() >= k) {
                    return result;
                }
            }
        }

        return {};


        // Attempt
        // // Step 1: count all nums frequency
        // unordered_map<int, int> count_map;
        // for (int i = 0; i < nums.size(); i++) {
        //     count_map[nums[i]] += 1;
        // }

        // // Step 2: sort count
        // vector<pair<int, int>> count_array;
        // for (auto i : count_map) {
        //     // cout << i.second << " " << i.first << endl;
        //     count_array.push_back(make_pair(i.second, i.first));
        // }
        // sort(count_array.rbegin(), count_array.rend());

        // // Step 3: return only k elements
        // vector<int> result;
        // for (int i = 0; i < k; i++) {
        //     result.push_back(count_array[i].second);
        // }

        // return result;
    }
};