class Solution {
public:
    int countOfPairs(vector<int>& nums) {
        for (std::array<std::array<int, 51>, 51>& i : m_Cache)
        {
            for (std::array<int, 51>& j : i)
            {
                j.fill(-1);
            }
        }

        return dfs(0, 0, 50, nums);
    }

    int dfs(int i, int previousIncreasing, int previousDecreasing, vector<int>& nums)
    {
        if (i >= nums.size())
        {
            return 1;
        }

        if (m_Cache[i][previousIncreasing][previousDecreasing] != -1)
        {
            return m_Cache[i][previousIncreasing][previousDecreasing];
        }

        int total = 0;
        for (int j = previousIncreasing; j <= nums[i]; j++)
        {
            int increasing = j;
            int decreasing = nums[i] - increasing;

            if (increasing >= previousIncreasing && decreasing <= previousDecreasing)
            {
                total = (total + dfs(i + 1, increasing, decreasing, nums)) % (int)(1e9 + 7);
            }
        }

        m_Cache[i][previousIncreasing][previousDecreasing] = total;

        return total;
    }

private:
    std::array<std::array<std::array<int, 51>, 51>, 2000> m_Cache = {};
};