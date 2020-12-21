# maybe test it out fist and then turn it into a Class...
"""
- confetti feature...
    - colors are random colors from block's colors
    - same size? or make different sizes and smaller ones fall slower
    - small skinny rectangles
    - falls from the top
    - ok it'd be cool if i had the words 'YOU WON' that fall with the confetti (at dif speeds) and have them rotate?
    - the words have a range of x values they can be, but they have to be int he correct order
    - make a confetti class?


"""

import pygame


class Confetti:
    def __init__(self, surface, x, y, size, color):
        self.surface = surface
        self.x = x
        self.y = y
        self.size = size  # input it as a tuple
        self.speed = size[0]/2  # adjust this... small size --> slow speed
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.size[0], self.size[1]))
        self.y += self.speed


class FallingLetters:
    def __init__(self, surface, text, x, y, speed):
        self.surface = surface
        self.text = text
        self.x = x
        self.y = y
        self.speed = speed
        self.font = pygame.font.Font("freesansbold.ttf", 25)

    def draw(self):
        text = self.font.render(self.text, True, (255, 255, 255))
        self.surface.blit(text, (self.x, self.y))
        self.y += self.speed
