class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // SECOND ATTEMPT (with NeetCode video)
        int left = 0;
        int right = numbers.size() - 1;
        int sum = numbers[left] + numbers[right];

        while (sum != target) {
            if (sum > target) {
                right -= 1;
            } else {
                left += 1;
            }

            sum = numbers[left] + numbers[right];
        }

        return {left + 1, right + 1};

        // FIRST ATTEMPT
        // // Index begin at 1
        // for (int i = 0; numbers.size() - 1; i++) {
        //     // Dichotomic search
        //     // a = i + 1 --> first element of subarray
        //     // b = numbers.size() - 1 --> last element of subarray
        //     int left = i + 1;
        //     int right = numbers.size() - 1;

        //     while (left <= right) {
        //         int middle = (left + right) / 2;

        //         // FOUND
        //         if (numbers[i] + numbers[middle] == target) {
        //             return { i + 1, middle + 1};
        //         } else if (numbers[i] + numbers[middle] > target) {
        //             right = middle - 1;
        //         } else {
        //             left = middle + 1;
        //         }
        //     }
        // }

        // return {0, 0};
    }
};