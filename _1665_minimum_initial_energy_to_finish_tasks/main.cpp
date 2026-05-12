class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        sort(begin(tasks), end(tasks), [&](auto& a, auto& b) {
            return a[1] - a[0] < b[1] - b[0];
        });

        int result = 0;
        for (const auto& task : tasks)
        {
            result = max(result + task[0], task[1]);
        }
        return result;
    }
};