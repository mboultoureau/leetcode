class Solution {
public:
    int dfs(
        int i,
        const string& colors,
        std::vector<std::vector<int>>& count,
        std::unordered_map<int, std::vector<int>>& neighbors,
        std::unordered_set<int>& path,
        std::unordered_set<int>& visited
    )
    {
        const int NB_COLORS = 26;

        // Graph contains cycle
        if (path.find(i) != path.end())
        {
            return -1;
        }

        if (visited.find(i) != visited.end())
        {
            return 0;
        }

        visited.insert(i);
        path.insert(i);

        int largest = 0;
        for (const int neighbor : neighbors[i])
        {
            if (dfs(neighbor, colors, count, neighbors, path, visited) == -1)
            {
                return -1;
            }

            for (int c = 0; c < NB_COLORS; c++)
            {
                count[i][c] = std::max(count[i][c], count[neighbor][c]);
                largest = std::max(largest, count[i][c]);
            }
        }

        count[i][colors[i] - 'a'] += 1;
        largest = std::max(largest, count[i][colors[i] - 'a']);

        path.erase(i);

        return largest;
    }


    int largestPathValue(string colors, vector<vector<int>>& edges) {
        const int NB_COLORS = 26;
        int largest = 0;
        int n = colors.size();

        std::vector<std::vector<int>> count(n, std::vector<int>(NB_COLORS, 0));
        std::unordered_map<int, std::vector<int>> neighbors(n);
        std::unordered_set<int> path;
        std::unordered_set<int> visited;

        for (const vector<int> edge : edges)
        {
            neighbors[edge[0]].push_back(edge[1]);
        }
        
        // DFS
        for (int i = 0; i < n; i++)
        {
            int result = dfs(i, colors, count, neighbors, path, visited);
            if (result == -1)
            {
                return -1;
            }
            largest = std::max(result, largest);
        }

        return largest;
    }
};