import pygame
from pygame.locals import *
from pygame.sprite import collide_rect

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)


class Ball:
    def __init__(self, screenWidth, screenHeight, size, xcord, ycord, xvelocity, yvelocity, color):
        self.size = 10
        self.color = color
        self.xcord = xcord
        self.ycord = ycord
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.rect = pygame.Rect(self.xcord, self.ycord, self.size, self.size)

    def move(self, paddle):
        if(self.ycord < 0 or self.ycord > self.screenHeight - self.size):
            self.yvelocity = -self.yvelocity
        if(self.rect.colliderect(paddle)):
            self.xvelocity = -self.xvelocity

        self.xcord += self.xvelocity
        self.ycord += self.yvelocity

        self.rect = pygame.draw.rect(screen, self.color,
                                     [self.xcord, self.ycord, self.size, self.size])


class Paddle:
    def __init__(self, screenWidth, screenHeight, size, xcord, ycord, color):
        self.size = 10
        self.color = color
        self.xcord = xcord
        self.ycord = ycord
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.move = 0
        self.rect = pygame.Rect(self.xcord, self.ycord,
                                self.size, self.size * 6)

    def draw(self):
        self.ycord += (self.move * 2)
        # don't go off the bottom of the screen
        if self.ycord > self.screenHeight - self.size * 6:  # if the ycord is off the screen
            self.ycord = self.screenHeight - self.size * 6  # reset the ycord to the bottom
            self.move = 0  # stop moving
        # don't go off the top of the screen:
        if self.ycord < 0:  # if the ycor is off the screen
            self.ycord = 0  # reset the ycor to the top
            self.move = 0  # stop moving

        self.rect = pygame.draw.rect(screen, self.color,
                                     [self.xcord, self.ycord, self.size, self.size * 6])


class Score:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.score = 0

    def increaseScore(self, value):
        self.score += value

    def displayScore(self):
        # This is a font we use to draw text on the screen (size 72)
        font = pygame.font.SysFont("911 Porscha", 72)
        text = font.render(str(self.score), True, WHITE)
        screen.blit(text, [self.xpos, self.ypos])

    def resetScore(self):
        self.score = 0


def draw_net(screenWidth, screenHeight):
    currentPos = 5
    while (currentPos < screenHeight):
        pygame.draw.rect(screen, WHITE,
                         [size[0] / 2, currentPos, 9, 9])
        currentPos += 20


clock = pygame.time.Clock()

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
ball_size = 10
ball_xstart = size[0] / 2
ball_ystart = size[1] / 2
ball_xvelocity = 3
ball_yvelocity = 3
ball_color = WHITE
screenWidth = size[0]
screenHeight = size[1]

ball = Ball(screenWidth, screenHeight, ball_size, ball_xstart, ball_ystart,
            ball_xvelocity, ball_yvelocity, ball_color)

paddle1_size = 10
paddle1_xstart = 25
paddle1_ystart = size[1] / 2
paddle1_color = WHITE
paddle1 = Paddle(screenWidth, screenHeight, paddle1_size,
                 paddle1_xstart, paddle1_ystart, paddle1_color)

paddle2_size = 10
paddle2_xstart = size[0] - 25
paddle2_ystart = size[1] / 2
paddle2_color = WHITE
paddle2 = Paddle(screenWidth, screenHeight, paddle2_size,
                 paddle2_xstart, paddle2_ystart, paddle2_color)

player1score = Score(screenWidth / 2 - 125, 25)
player2score = Score(screenWidth / 2 + 100, 25)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                paddle2.move += -5
            if event.key == K_w:
                paddle1.move += -5
            if event.key == K_DOWN:
                paddle2.move += 5
            if event.key == K_s:
                paddle1.move += 5
        if event.type == pygame.KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                paddle2.move = 0
            if event.key == K_w or event.key == K_s:
                paddle1.move = 0

    screen.fill(BLACK)
    if(ball.xcord < 0):
        ball.xcord = screenWidth / 2
        ball.ycord = screenHeight / 2
        ball.xvelocity = -ball.xvelocity
        player1score.increaseScore(1)
    if(ball.xcord > ball.screenWidth - ball.size):
        ball.xcord = screenWidth / 2
        ball.ycord = screenHeight / 2
        ball.xvelocity = -ball.xvelocity
        player2score.increaseScore(1)

    # draw here:
    draw_net(size[0], size[1])
    for paddle in [paddle1, paddle2]:
        ball.move(paddle)
    paddle1.draw()
    paddle2.draw()
    player1score.displayScore()
    player2score.displayScore()

    if player1score.score == 5 or player2score.score == 5:
        # start "waiting" for a response
        waiting = True
        while waiting:
            # display the Game Over text
            font = pygame.font.Font(None, 36)
            text = font.render("GAME OVER. PLAY AGAIN? Y/N ", True, WHITE)
            screen.blit(text, [200, 250])
            for event in pygame.event.get():  # check keystrokes
                if event.type == pygame.KEYDOWN:  # if a key is pressed
                    if event.key == K_y:  # if player presses Y for "yes"
                        player1score.resetScore()  # reset the scores
                        player2score.resetScore()
                        waiting = False
                        break
                    if event.key == K_n:  # if player presses N for "no"
                        waiting = False
                        done = True  # game is done
                        break
            pygame.display.update()  # keep refreshing screen while waiting

    # update the screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()
