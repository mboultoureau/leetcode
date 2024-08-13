class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> current;
        backtracking(candidates, target, 0, current);
        return m_Result;
    }

    void backtracking(vector<int>& candidates, int target, int i, vector<int>& current)
    {
        if (target == 0)
        {
            m_Result.push_back(current);
            return;
        }

        if (i == candidates.size() || target < 0)
        {
            return;
        }

        current.push_back(candidates[i]);
        target -= candidates[i];
        backtracking(candidates, target, i + 1, current);

        // While is the same number
        while (i + 1 < candidates.size() && candidates[i] == candidates[i + 1])
        {
            i += 1;
        }

        current.pop_back();
        target += candidates[i];
        backtracking(candidates, target, i + 1, current);
    }

private:
    vector<vector<int>> m_Result;
};