class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> answer;
        answer.reserve(queries.size());

        int current_sum = 0;
        for (const int n : nums) {
            if (n % 2 == 0) {
                current_sum += n;
            }
        }
        
        for (const auto& query : queries) {
            int val = query[0];
            int index = query[1];

            if (nums[index] % 2 == 0) {
                current_sum -= nums[index];
            }

            nums[index] = nums[index] + val;

            if (nums[index] % 2 == 0) {
                current_sum += nums[index];
            }

            answer.push_back(current_sum);
        }

        return answer;
    }
};