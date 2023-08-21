class Solution {
public:
    bool isPalindrome(string s) {
        // THIRD ATTEMPT (with NeetCode video)
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            while (left < right && !isalnum(s[left])) {
                left += 1;
            }

            while (right > left && !isalnum(s[right])) {
                right -= 1;
            }

            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }

            left += 1;
            right -= 1;
        }

        return true;

        // SECOND ATTEMPT: compare with reverse string
        // string str = "";
        // for (char c : s) {
        //     if ((c >= 'a' && c <= 'z') || c >= '0' && c <= '9') {
        //         str += c;
        //     } else if (c >= 'A' && c <= 'Z') {
        //         str += c - 'A' + 'a';
        //     }
        // }

        // return equal(str.rbegin(), str.rend(), str.begin());




        // FIRST ATTEMPT
        // First step: convert to lowercase
        // string str = "";
        // for (char c : s) {
        //     if ((c >= 'a' && c <= 'z') || c >= '0' && c <= '9') {
        //         str += c;
        //     } else if (c >= 'A' && c <= 'Z') {
        //         str += c - 'A' + 'a';
        //     }
        // }

        // // Second step: compare
        // int i = 0;
        // int j = str.size() - 1;

        // while (i < j) {
        //     if (str[i] != str[j]) {
        //         return false;
        //     }
        //     i++;
        //     j--;
        // }

        // return true;
    }
};