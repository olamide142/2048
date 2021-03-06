# ==========================================
# Title:  2048 GAME
# Author: Olamide V.O
# Date:   10 Jan 2021
# ==========================================

import sys
import random

import pygame
import numpy as np

from movement import *

# constants
COLOR = {'GRID_PRI': (220, 254, 220),
         'GRID_SEC': (146, 169, 146),
         'TXT_SEC': (48, 56, 48),
         'TXT_PRI': (48, 48, 56)}


class Grid:
    
    def __init__(self):
        pass

    def run(self):

        pygame.draw.rect(screen, COLOR['TXT_SEC'], (55, 130, 310, 300), 4)
        for x in range(1, 5):
            for y in range(2, 6):
                rect = pygame.Rect(x * Box.size, y * Box.size,
                                   Box.size, Box.size)
                pygame.draw.rect(screen, COLOR['TXT_SEC'], rect, 1)



class Content:
    
    def __init__(self):
        self.score = 0
        self.best = 0

    def update_best(self, data):
        self.best += data
        # update db

    def update_score(self, data):
        self.score += data
        if self.score > self.best:
            self.update_best(
                self.score
            )

    def run(self):
        global font_size
        font_size = {'BIG': pygame.font.Font(None, 72),
                     'MEDIUM': pygame.font.Font(None, 36),
                     'SMALL': pygame.font.Font(None, 18)}
        pygame.draw.rect(
            screen, COLOR['GRID_SEC'], (0, 0, 480, 100))
        score_board = pygame.draw.rect(
            screen, COLOR['TXT_SEC'], (350, 0, 260, 100))

        length = score_board.right - score_board.left
        screen.blit(font_size['MEDIUM'].render(
            "Score:", True, COLOR['GRID_PRI']), (score_board.left + 5, 15))
        screen.blit(font_size['BIG'].render(
            str(self.score), True, COLOR['GRID_PRI']), (score_board.left + 20, 50))

        screen.blit(font_size['BIG'].render(
            "2048", True, COLOR['TXT_SEC']), (25, 25))


class Game:
    __size_x = 500
    __size_y = 500
    clock = pygame.time.Clock()

    def __init__(self):
        self.setup()

    def setup(self) -> None:
        pygame.init()
        pygame.display.set_caption("2048 - github: olamide142")
        global screen
        screen = pygame.display.set_mode((
            self.__size_x,
            self.__size_y
        ))

    def run(self):
        screen.fill(COLOR['GRID_PRI'])


class Box:
    size = 70
    boxes = [
        [0, 50, 50, 0],
        [0, 50, 70, 0],
        [0, 0, 70, 0],
        [0, 0, 80, 0]
    ]

    def __init__(self, position=0):
        self.gen_starting_box()

    def gen_starting_box(self):

        a = random.choice(self.generate_random_position())
        b = random.choice(self.generate_random_position())

        if all((Box.can_render(a), Box.can_render(b),  a != b)):
            Box.boxes[a[0]][a[1]] = random.choice([2, 4])
            Box.boxes[b[0]][b[1]] = random.choice([2, 4])

    def generate_random_position(self):

        for i in range(len(Box.boxes)):
            for  j in Box.boxes[i]:
                if j == 0:
                    return tuple((i, j))

    def run(self):
        for x, i in enumerate(Box.boxes):
            # print(x,i)
            for y in i:
                rect = pygame.Rect(x * Box.size, y * Box.size,
                                   Box.size - 4, Box.size - 4)
                if Box.can_render(y):
                    print(i)
                screen.blit(font_size['BIG'].render("OLamide", True, COLOR['GRID_PRI']), (20, 50))
                    screen.blit(font_size['MEDIUM'].render("str(y)",
                    True, COLOR['TXT_PRI']), (rect.left + 25 // 2, rect.bottom - 35))



    @staticmethod
    def can_render(data):
        return data != 0

    @staticmethod
    def move(key):

        a = [Box.boxes[i][0] for i in range(4)]
        b = [Box.boxes[i][1] for i in range(4)]
        c = [Box.boxes[i][2] for i in range(4)]
        d = [Box.boxes[i][3] for i in range(4)]
        
        data = (a, b, c, d)
        print(a)
        if key == pygame.K_UP:
            Movement(data).up()
        elif key == pygame.K_DOWN: 
            Movement(data).down()
        elif key == pygame.K_LEFT: 
            Movement(data).left()
        elif key == pygame.K_RIGHT: 
            Box.boxes = Movement(data).right()
            np.array(Box.boxes).tolist()




# 2048
game = Game()
content = Content()
grid = Grid()
box = Box()

while 1:

    Game.clock.tick(60)
    game.run()
    content.run()
    grid.run()
    box.run()

    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            Box.move(event.key)

        if event.type == pygame.QUIT:
            pygame.quit()
