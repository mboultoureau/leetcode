class Solution {
public:
    string decodeString(string s) {
        // SECOND ATTEMPT (NeetCode video)
        string decoded = "";

        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ']') {
                decoded += s[i];
            } else {
                string substring = "";

                while (decoded.back() != '[') {
                    substring += decoded.back();
                    decoded.pop_back();
                }
                reverse(substring.begin(), substring.end());

                // Remove [
                decoded.pop_back();

                string k = "";
                while (decoded.size() > 0 && isdigit(decoded.back())) {
                    k += decoded.back();
                    decoded.pop_back();
                }
                reverse(k.begin(), k.end());

                int repeats = stoi(k);
                for (int j = 0; j < repeats; j++) {
                    decoded += substring;
                }
            }
        }

        return decoded;

        // FIRST ATTEMPT
        // string decoded = "";

        // for (int i = 0; i < s.size(); i++) {
        //     if (isalpha(s.at(i))) {
        //         decoded += s.at(i);
        //     } else {
        //         string content = "";
        //         string nb = "";

        //         while (isdigit(s.at(i))) {
        //             nb += s.at(i);
        //             i++;
        //         }
        //         i++;

        //         int open = 1;
        //         while (open != 1 || s.at(i) != ']') {
        //             if (s.at(i) == '[') {
        //                 open++;
        //             } else if (s.at(i) == ']') {
        //                 open--;
        //             }

        //             content += s.at(i);
        //             i++;
        //         }

        //         int repetitions = stoi(nb);
        //         string substring = decodeString(content);

        //         for (int j = 0; j < repetitions; j++) {
        //             decoded += substring;
        //         }
        //     }
        // }

        // return decoded;
    }
};