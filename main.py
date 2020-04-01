from character import Character
from map import Map

import pygame
import math

pygame.init()

map = Map()
character = Character()

gameDisplay = pygame.display.set_mode((map.width, map.height))
pygame.display.set_caption('game_test')

clock = pygame.time.Clock()
crashed = False
upPress = False
downPress = False
rightPress = False
leftPress = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True
            elif event.key == pygame.K_UP:
                upPress = True
            elif event.key == pygame.K_DOWN:
                downPress = True
            elif event.key == pygame.K_RIGHT:
                rightPress = True
            elif event.key == pygame.K_LEFT:
                leftPress = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                upPress = False
            elif event.key == pygame.K_DOWN:
                downPress = False
            elif event.key == pygame.K_RIGHT:
                rightPress = False
            elif event.key == pygame.K_LEFT:
                leftPress = False

    if upPress:
        map.updateImage(character)
        character.updateImage(1)
        character.updatePosition(-1)

    if downPress:
        map.updateImage(character)
        character.updateImage(-1)
        character.updatePosition(1)

    if rightPress:
        character.changeRotation(-10)

    if leftPress:
        character.changeRotation(10)


    gameDisplay.blit(map.image, (0, 0))
    gameDisplay.blit(character.image, character.getScreenPosition(map))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
