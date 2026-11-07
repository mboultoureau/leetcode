class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        using pair_int = pair<int, int>;

        const int n = servers.size();
        const int m = tasks.size();
        long long time = 0;

        vector<int> answers;
        answers.reserve(m);

        priority_queue<pair_int, vector<pair_int>, greater<pair_int>> running;
        priority_queue<pair_int, vector<pair_int>, greater<pair_int>> idle;

        for (int i = 0; i < n; ++i) {
            idle.emplace(servers[i], i);
        }

        auto liberate = [&]() {
            while (!running.empty() && running.top().first <= time) {
                int index = running.top().second;
                idle.emplace(servers[index], index);
                running.pop();
            }
        };

        for (int j = 0; j < m; ++j) {
            time = max(time, static_cast<long long>(j));
            liberate();

            if (idle.empty()) {
                time = running.top().first;
                liberate();
            }
        
            int index = idle.top().second;
            answers.push_back(index);
            running.emplace(time + tasks[j], index);
            idle.pop();
        }

        return answers;
    }
};