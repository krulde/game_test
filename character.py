import pygame
import math

class Character:
    def __init__(self):
        self.position = (0, 0)
        self.rotation = 0
        self.current = 0
        self.cycle = []
        self.range = 200
        self.yChange = 0

        for i in range(26):
            iStr = str(i + 5)
            while len(iStr) < 4:
                iStr = '0' + iStr
            self.cycle.append(pygame.image.load('walk_cycle_test/Walk_cycle_loop' + iStr + '.png'))
        self.image = self.cycle[self.current]

    def changeRotation(self, rotationChange):
        self.rotation += rotationChange
        self.rotation % 360
        self.updateImage(0)

    def updatePosition(self, value):
        newxPos = self.position[0] + value * 10 * math.sin(math.radians(self.rotation))
        newyPos = self.position[1] + value * 10 * math.cos(math.radians(self.rotation))
        if abs(newxPos) > self.range:
            if newxPos < 0:
                newxPos = self.range * -1
            else:
                newxPos = self.range
        if abs(newyPos) > self.range:
            self.yChange = newyPos - self.position[1]
            if newyPos < 0:
                newyPos = self.range * -1
            else:
                newyPos = self.range
        else:
            self.yChange = 0
        self.position = (newxPos, newyPos)
        print(self.position)



    def updateImage(self, value):
        if value > 0:
            self.current += 1
            if self.current > 25:
                self.current = 0
        elif value < 0:
            self.current -= 1
            if self.current < 0:
                self.current = 25
        self.image = self.cycle[self.current]
        self.image = pygame.transform.rotate(self.image, self.rotation)

    def getScreenPosition(self, map):
        rect = self.image.get_rect()
        x = map.width * 0.5 - rect.width * 0.5
        y = map.height * 0.5 - rect.height * 0.5
        x += self.position[0]
        y += self.position[1]
        return(x, y)
