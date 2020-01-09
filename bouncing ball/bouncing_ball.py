# pygame_template.py

from random import randint

import pygame


class Ball:
    def __init__(self, screenWidth, screenHeight, radius, xcord, ycord, xvelocity, yvelocity, color):
        self.radius = 10
        self.color = color
        self.xcord = xcord
        self.ycord = ycord
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def move(self):
        if(self.xcord < 0 or self.xcord > self.screenWidth - self.radius):
            self.xvelocity = -self.xvelocity
        if(self.ycord < 0 or self.ycord > self.screenHeight - self.radius):
            self.yvelocity = -self.yvelocity

        self.xcord += self.xvelocity
        self.ycord += self.yvelocity

        pygame.draw.ellipse(screen, self.color,
                            [self.xcord, self.ycord, 2*self.radius, 2*self.radius])


# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)


clock = pygame.time.Clock()

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Balls")

ball_list = []
for index in range(0, 10):
    ball = Ball(size[0], size[1], 10, randint(
        0, size[0]), randint(0, size[1]), 3, 4, WHITE)
    ball_list.append(ball)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # draw here:
    for ball in ball_list:
        ball.move()

    # update the screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()
