class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        return fitBook(0, books, shelfWidth);
    }

private:
    std::map<int, int> m_Cache;

    int fitBook(int i, vector<vector<int>>& books, int shelfWidth)
    {
        // Base case
        if (i == books.size())
        {
            return 0;
        }

        // Check in cache
        if (m_Cache.contains(i))
        {
            return m_Cache[i];
        }

        int width = 0;
        int height = 0;
        int best = 1000 * 1000;
        for (int j = i; j < books.size(); j++)
        {
            if (books[j][0] + width > shelfWidth)
            {
                break;
            }

            width += books[j][0];
            height = max(height, books[j][1]);
            best = min(best, height + fitBook(j + 1, books, shelfWidth));
        }

        m_Cache.insert(std::pair<int, int>(i, best));

        return best;
    }
};