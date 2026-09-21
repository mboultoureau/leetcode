class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        std::vector<long long> answer(k, 0);
        std::vector<long long> prev(k, 0);
        std::vector<long long> current(k, 0);

        for (int i = 0; i < nums.size(); ++i)
        {
            int n = (nums[i] % k);

            std::fill(current.begin(), current.end(), 0LL);
            current[n]++;

            for (int j = 0; j < k; ++j)
            {
                if (prev[j] > 0)
                {
                    current[(n * j) % k] += prev[j];
                }
            }

            for (int j = 0; j < k; ++j)
            {
                answer[j] += current[j];
            }


            prev = current;
        }

        return answer;
    }
};