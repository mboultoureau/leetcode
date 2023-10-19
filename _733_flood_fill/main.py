class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        oldColor = image[sr][sc]
        image[sr][sc] = color

        if (sr >= 1 and oldColor == image[sr - 1][sc]):
            self.floodFill(image, sr - 1, sc, color)

        if (sr < len(image) - 1 and oldColor == image[sr + 1][sc]):
            self.floodFill(image, sr + 1, sc, color)

        if (sc >= 1 and oldColor == image[sr][sc - 1]):
            self.floodFill(image, sr, sc - 1, color)

        if (len(image) > 0 and sc < len(image[0]) - 1 and oldColor == image[sr][sc + 1]):
            self.floodFill(image, sr, sc + 1, color)

        return image
