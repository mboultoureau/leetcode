class Solution {
public:
    int dfs(unordered_map<int, unordered_set<int>>& graph, int node, int parent, int k)
    {
        if (k < 0)
        {
            return 0;
        }

        int count = 1;
        for (const int neighbor : graph[node])
        {
            if (neighbor == parent)
            {
                continue;
            }
            count += dfs(graph, neighbor, node, k - 1);
        }

        return count;
    }


    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        vector<int> answers(edges1.size() + 1);
        unordered_map<int, unordered_set<int>> graph1;
        unordered_map<int, unordered_set<int>> graph2;

        for (const vector<int>& edge : edges1)
        {
            graph1[edge[0]].insert(edge[1]);
            graph1[edge[1]].insert(edge[0]);
        }

        for (const vector<int>& edge : edges2)
        {
            graph2[edge[0]].insert(edge[1]);
            graph2[edge[1]].insert(edge[0]);
        }

        int maxGraph2 = 0;
        for (const auto& pair : graph2)
        {
            maxGraph2 = max(maxGraph2, dfs(graph2, pair.first, -1, k - 1));
        }

        for (int i = 0; i < edges1.size() + 1; i++)
        {
            answers[i] = dfs(graph1, i, -1, k) + maxGraph2;
        }

        return answers;
    }
};