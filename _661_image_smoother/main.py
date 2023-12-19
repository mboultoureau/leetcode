class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        smoothImg = []
        for r in range(m):
            row = []
            for c in range(n):
                square = [img[r][c]]
                if r > 0:
                    # Top left
                    if c > 0:
                        square.append(img[r - 1][c - 1])
                    # Top
                    square.append(img[r - 1][c])

                    # Top right
                    if c < n - 1:
                        square.append(img[r - 1][c + 1])

                # Left
                if c > 0:
                    square.append(img[r][c - 1])
                # Right
                if c < n - 1:
                    square.append(img[r][c + 1])

                # Bottom left
                if r < m - 1:
                    if c > 0:
                        square.append(img[r + 1][c - 1])
                    # Bottom
                    square.append(img[r + 1][c])
                    # Bottom right
                    if c < n - 1:
                        square.append(img[r + 1][c + 1])

                row.append(floor(sum(square) / len(square)))

            smoothImg.append(row)

        return smoothImg