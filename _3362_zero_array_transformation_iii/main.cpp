class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        // Resolved with the help of the solution
        int count = 0;
        int j = 0;
        priority_queue<int> available;
        priority_queue<int, vector<int>, greater<int>> allocated;

        sort(queries.begin(), queries.end());

        for (int i = 0; i < nums.size(); i++)
        {
            // Remove all expired allocations
            while (!allocated.empty() && allocated.top() < i)
            {
                allocated.pop();
            }

            // Add all new allocations to available corresponding with current time
            while (j < queries.size() && queries[j][0] <= i)
            {
                available.push(queries[j][1]);
                j++;
            }

            // Count possible allocations
            while (allocated.size() < nums[i] && !available.empty() && available.top() >= i)
            {
                allocated.push(available.top());
                available.pop();
                count++;
            }

            // If can't have 0 array
            if (allocated.size() < nums[i])
            {
                return -1;
            }
        }

        return queries.size() - count;
    }
};