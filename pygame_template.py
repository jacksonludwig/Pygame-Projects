# pygame_template.py

import pygame

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Template")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # fill the screen with background color
    screen.fill(WHITE)

    # draw here:
    # pygame.draw.rect(screen, RED, [100, 200, 50, 80], 0)
    # pygame.draw.rect(screen,RED,[100,200,50,80],2)

    # update the screen
    pygame.display.update()

pygame.quit()
