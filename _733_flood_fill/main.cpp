class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] == color)
        {
            return image;
        }

        int current = image[sr][sc];
        image[sr][sc] = color;

        // Up
        if (sr >= 1 && current == image[sr - 1][sc])
        {
            floodFill(image, sr - 1, sc, color);
        }

        // Down
        if (sr < image.size() - 1 && current == image[sr + 1][sc])
        {
            floodFill(image, sr + 1, sc, color);
        }

        // Left
        if (sc >= 1 && current == image[sr][sc - 1])
        {
            floodFill(image, sr, sc - 1, color);
        }

        // Right
        if (image.size() > 0 && sc < image[0].size() - 1 && current == image[sr][sc + 1])
        {
            floodFill(image, sr, sc + 1, color);
        }
        
        return image;
    }
};