class Solution {
public:
    int minimumDeletions(string s) {
        int solution = std::pow(10, 5);
        int prefix = 0; // Number of "a" before the separator
        int suffix = 0; // Number of "b" after the separator

        // Calculate number of "b" after the separator
        for (char& c : s)
        {
            if (c == 'b')
            {
                suffix += 1;
            }
        }

        // We bruteforce the position of separation between the "a" and "b"
        for (int separator = 0; separator <= s.size(); separator++)
        {
            // Number of characters to delete
            int b_to_deleted = separator - prefix;
            int a_to_deleted = (s.size() - separator) - suffix;
            int to_deleted = a_to_deleted + b_to_deleted;

            solution = std::min(to_deleted, solution);

            // Update suffix and prefix
            if (separator == s.size())
            {
                break;
            }

            if (s[separator] == 'a')
            {
                prefix += 1;
            }
            else
            {
                suffix -= 1;
            }
        }

        return solution;
    }
};