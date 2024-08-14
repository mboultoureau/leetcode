class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int size = nums.size();
        int maximum = nums[size - 1]; 
        
        vector<int> prefix(maximum * 2, 0);
        unordered_map<int, int> counter;

        int i = 0;
        for (int value = 0; value < maximum * 2; value++)
        {
            while (i < size && nums[i] <= value) {
                i++;
            }
            prefix[value] = i;
        }

        for (int i = 0; i < size; i++)
        {
            counter[nums[i]]++;
        }

        int left = 0;
        int right = maximum;
        while (left < right)
        {
            int middle = (left + right) / 2;

            int count = 0;
            i = 0;

            while (i < size)
            {
                int current = counter[nums[i]];
                int larger = prefix[nums[i] + middle] - prefix[nums[i]];
                int same = current * (current - 1) / 2;

                count += larger * current + same;

                while (i + 1 < size && nums[i] == nums[i + 1])
                {
                    i++;
                }

                i++;
            }

            if (count < k) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }

        return left;

        // Time limit exceeded
        // std::priority_queue<int> heap;

        // for (int i = 0; i < nums.size(); i++)
        // {
        //     for (int j = i + 1; j < nums.size(); j++)
        //     {
        //         heap.push(abs(nums[i] - nums[j]));
        //         if (heap.size() > k)
        //         {
        //             heap.pop();
        //         }
        //     }
        // }

        // return heap.top();
    }
};