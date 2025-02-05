class Solution
{
public:
    bool dfs(int i, std::array<int, 4>& sides, vector<int> const& matchsticks, int sideSum)
    {
        if (i == matchsticks.size()) {
            return sides[0] == sides[1] && sides[1] == sides[2] && sides[2] == sideSum;
        }

        for (int s = 0; s < 4; s++)
        {
            if (sides[s] + matchsticks[i] <= sideSum)
            {
                sides[s] += matchsticks[i];
                if (dfs(i + 1, sides, matchsticks, sideSum)) {
                    return true;
                }

                sides[s] -= matchsticks[i];
            }
        }

        return false;
    }

    bool makesquare(vector<int>& matchsticks)
    {
        int sum = 0;
        for (auto& matchstick : matchsticks)
        {
            sum += matchstick;
        }

        // if no matchtsicks or no divisible by 4
        if (sum % 4 != 0 || sum == 0)
        {
            return false;
        }

        std::sort(matchsticks.begin(), matchsticks.end(), std::greater<>());
        std::array<int, 4> sides = {0, 0, 0, 0};

        return dfs(0, sides, matchsticks, sum / 4);
    }
};