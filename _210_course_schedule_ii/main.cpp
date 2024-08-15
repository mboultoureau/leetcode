class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Parse prerequisites
        for (vector<int>& prerequisite : prerequisites)
        {
            if (!m_Requirements.contains(prerequisite[0]))
            {
                m_Requirements.emplace(prerequisite[0], vector<int>());
            }

            m_Requirements[prerequisite[0]].push_back(prerequisite[1]);
        }

        std::unordered_set<int> path;
        for (int i = 0; i < numCourses; i++)
        {
            if (dfs(numCourses, path, i) == false)
            {
                return vector<int>();
            }
        }

        return m_Result;
    }

    bool dfs(int numCourses, std::unordered_set<int>& path, int start)
    {
        if (path.contains(start))
        {
            return false;
        }

        if (m_Visited.contains(start))
        {
            return true;
        }

        if (!m_Requirements.contains(start))
        {
            m_Visited.insert(start);
            m_Result.push_back(start);
            return true;
        }

        for (int requirement : m_Requirements[start])
        {
            path.insert(start);
            if (!dfs(numCourses, path, requirement)) {
                return false;
            }
            path.erase(start);
        }

        m_Visited.insert(start);
        m_Result.push_back(start);

        return true;
    }

private:
    std::unordered_map<int, vector<int>> m_Requirements;
    std::unordered_set<int> m_Visited;
    std::vector<int> m_Result;
};