class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int metal = 0;
        int paper = 0;
        int glass = 0;

        for (int i = garbage.size() - 1; i >= 0; i--)
        {
            for (char& c : garbage[i])
            {
                switch (c)
                {
                    case 'M':
                        metal += 1;
                        break;
                    case 'P':
                        paper += 1;
                        break;
                    case 'G':
                        glass += 1;
                        break;
                }
            }

            if (i <= 0)
            {
                continue;
            }

            if (metal != 0)
            {
                metal += travel[i - 1];
            }

            if (paper != 0)
            {
                paper += travel[i - 1];
            }

            if (glass != 0)
            {
                glass += travel[i - 1];
            }
        }

        return metal + paper + glass;
    }
};