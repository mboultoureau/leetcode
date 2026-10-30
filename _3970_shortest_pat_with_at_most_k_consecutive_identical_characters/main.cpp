class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        vector<vector<pair<int, int>>> links(n);
        for (const vector<int> edge : edges) {
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            
            links[start].emplace_back(end, weight);
        }
        
        vector<vector<int>> distance(n, vector<int>(k + 1, numeric_limits<int>::max()));
        distance[0][1] = 0;

        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> unvisited;
        unvisited.emplace(0, 1, 0);

        while(!unvisited.empty()) {
            auto [dist, count, node] = unvisited.top();
            unvisited.pop();

            if (dist > distance[node][count]) {
                continue;
            }

            if (node == n - 1) {
                return dist;
            }

            for (const auto [end, weight] : links[node]) {
                int new_count = labels[node] == labels[end] ? count + 1 : 1;

                if (new_count > k) {
                    continue;
                }

                int new_distance = dist + weight;

                if (new_distance < distance[end][new_count]) {
                    distance[end][new_count] = new_distance;
                    unvisited.emplace(new_distance, new_count, end);
                }
            }

        }

        return -1;
    }
};