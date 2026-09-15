class Solution {
public:
    bool isPalindrome(string& s, int i, int j) {
        while (i < j) {
            if (s[i] != s[j]) {
                return false;
            }

            i++;
            j--;
        }

        return true;
    }

    int maxPalindromes(string s, int k) {
        int count = 0;

        int i = 0;
        while (i <= s.size() - k) {
            if (isPalindrome(s, i, i + k - 1)) {
                count++;
                i = i + k;
                continue;
            }

            if (isPalindrome(s, i, i + k)) {
                count++;
                i = i + k + 1;
                continue;
            }

            i++;
        }

        return count;
    }
};