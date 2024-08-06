class Solution {
public:
    int minimumPushes(string word) {
        std::array<int, 26> count = {};
        for (const char& c : word)
        {
            count[c - 'a'] += 1;
        }

        std::sort(std::begin(count), std::end(count), std::greater<>());

        int pushes = 0;
        for (int i = 0; i < 8; i++)
        {
            pushes += count[i];
        }

        for (int i = 8; i < 16; i++)
        {
            pushes += count[i] * 2;
        }

        for (int i = 16; i < 24; i++)
        {
            pushes += count[i] * 3;
        }

        for (int i = 24; i < 26; i++)
        {
            pushes += count[i] * 4;
        }

        return pushes;
    }
};