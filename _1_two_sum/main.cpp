class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numbers;

        for (int i = 0; i < nums.size(); i++) {
            int searchedNumber = target - nums[i];
            if (numbers.find(searchedNumber) != numbers.end()) {
                return { numbers[searchedNumber], i };
            }
            numbers[nums[i]] = i; 
        }

        return {0, 0};

        // First attempt: brute-force
        // vector<int> positions;

        // for (int i = 0; i < nums.size(); i++) {
        //     for (int j = i; j < nums.size(); j++) {
        //         if (i == j) continue;

        //         if (nums[i] + nums[j] == target) {
        //             positions.push_back(i);
        //             positions.push_back(j);

        //             return positions;
        //         }
        //     }
        // }

        // return positions;
    }
};