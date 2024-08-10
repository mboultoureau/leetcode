class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        std::vector<int> result;
        std::set<int> set;
        for (int i = 0; i < n; i++)
        {
            set.insert(i);
        }

        for (const vector<int>& query : queries)
        {
            set.erase(set.lower_bound(query[0] + 1), set.upper_bound(query[1] - 1));
            result.push_back(set.size() - 1);
        }

        return result;
    }
};