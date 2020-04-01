import pygame

class Map:
    def __init__(self):
        self.current = 0
        self.mapImages = []
        self.width = 1920
        self.height = 1080
        self.storedChange = 0
        for i in range(191):
            iStr = str(i)
            while len(iStr) < 4:
                iStr = '0' + iStr
            self.mapImages.append(pygame.image.load('game_city_z_test/Game_z_test' + iStr + '.png'))
        self.image = self.mapImages[self.current]

    def updateImage(self, character):
        if character.yChange < 0:
            if character.yChange + self.storedChange < -5:
                self.current += 1
                if self.current > 190:
                    self.current = 190
                character.yChange = 0
                self.storedChange = 0
                self.image = self.mapImages[self.current]
            else:
                self.storedChange += character.yChange
        if character.yChange > 0:
            if character.yChange + self.storedChange > 5:
                self.current -= 1
                if self.current < 0:
                    self.current = 0
                character.yChange = 0
                self.storedChange = 0
                self.image = self.mapImages[self.current]
            else:
                self.storedChange += character.yChange
