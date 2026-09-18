class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        // For each char, associate start and end
        const int NB_LETTERS = 26;
        vector<pair<int, int>> charSubstrings(NB_LETTERS, {-1, -1});

        for (int i = 0; i < s.size(); ++i)
        {
            int c = s[i] - 'a';

            if (charSubstrings[c].first == -1)
            {
                charSubstrings[c] = {i, i};
            }
            else
            {
                charSubstrings[c].second = i;
            }
        }

        // Expand to include all occurences of the character in the string
        for (int l = 0; l < NB_LETTERS; ++l)
        {
            if (charSubstrings[l].first == -1) continue;

            for (int i = charSubstrings[l].first; i <= charSubstrings[l].second; ++i)
            {
                int c = s[i] - 'a';

                if (charSubstrings[l].first <= charSubstrings[c].first && charSubstrings[l].second >= charSubstrings[c].second)
                {
                    continue;
                }

                charSubstrings[l] = {
                    min(charSubstrings[l].first, charSubstrings[c].first),
                    max(charSubstrings[l].second, charSubstrings[c].second)
                };

                i = charSubstrings[l].first;
            }
        }

        sort(charSubstrings.begin(), charSubstrings.end(), [](auto a, auto b) {
            return a.second < b.second;
        });

        vector<string> output;
        int last = -1;

        for (auto [left, right] : charSubstrings)
        {
            if (left > last) {
                output.push_back(s.substr(left, right - left + 1));
                last = right;
            }
        }

        return output;
    }
};