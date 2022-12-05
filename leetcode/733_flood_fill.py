class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        oldColor = image[sr][sc]
        
        if oldColor != color:
            image = self.changeColor(image, sr, sc, color, oldColor)
        return image

    def changeColor(self, image: list[list[int]], sr: int, sc: int, color: int, oldColor: int) -> list[list[int]]:
        if (sr > -1 and sc > -1 and sr < len(image) and sc < len(image[0]) and image[sr][sc] == oldColor):
            image[sr][sc] = color
        
            image = self.changeColor(image, sr - 1, sc, color, oldColor)
            image = self.changeColor(image, sr + 1, sc, color, oldColor)
            image = self.changeColor(image, sr, sc - 1, color, oldColor)
            image = self.changeColor(image, sr, sc + 1, color, oldColor)

        return image
