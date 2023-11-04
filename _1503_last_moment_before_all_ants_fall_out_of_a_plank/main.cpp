class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        // Solution 2
        int time = 0;
        for (int i : left)
        {
            time = max(time, i);
        }

        for (int i : right)
        {
            time = max(time, n - i);
        }

        return time;

        // Solution 1
        // int time = -1;
        // while (left.size() != 0 || right.size() != 0)
        // {
        //     time++;

        //     // --->
        //     for (auto it = right.begin(); it != right.end();)
        //     {
        //         if (*it == n)
        //         {
        //             it = right.erase(it);
        //         }
        //         else
        //         {
        //             (*it)++;
        //             ++it;
        //         }
        //     }

        //     // <---
        //     for (auto it = left.begin(); it != left.end();)
        //     {
        //         if (*it == 0)
        //         {
        //             it = left.erase(it);
        //         }
        //         else
        //         {
        //             (*it)--;
        //             ++it;
        //         }
        //     }
        // }

        // return time;
    }
};