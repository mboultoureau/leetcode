class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> nums = {1};
        int i2 = 0;
        int i3 = 0;
        int i5 = 0;

        for (int i = 0; i < n; i++)
        {
            int next = std::min(
                nums[i2] * 2,
                std::min(
                    nums[i3] * 3,
                    nums[i5] * 5
                )
            );
            nums.push_back(next);

            if (next == nums[i2] * 2) {
                i2++;
            }

            if (next == nums[i3] * 3) {
                i3++;
            }

            if (next == nums[i5] * 5) {
                i5++;
            }
        }

        return nums[n - 1];

        // std::unordered_set<long> visited;
        // std::priority_queue<long, std::vector<long>, std::greater<long>> candidates;
        // std::array<int, 3> factors = {2, 3, 5};

        // candidates.push(1);
        // long top = 0;

        // for (int i = 0; i < n; i++)
        // {
        //     top = candidates.top();
        //     candidates.pop();

        //     for (const int& factor : factors)
        //     {
        //         if (!visited.contains(top * factor))
        //         {
        //             visited.insert(top * factor);
        //             candidates.push(top * factor);
        //         }
        //     }
        // }

        // return (int)top;
    }
};