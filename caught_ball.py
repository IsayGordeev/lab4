import pygame
from pygame.draw import *
from random import randint, choice, random
import math

from pygame.transform import rotate

pygame.init()
pygame.font.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800
Score_size = 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
labelFont = pygame.font.SysFont('Helvetic', Score_size)
finished = False
print('Enter your Nickname')
a = input()
out = open('Scores_data', 'a')

WHITE = (255, 255, 255)
MILDERGREY = (190, 190, 190)
MILDGREY = (211, 211, 211)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]


class Ball:
    def __init__(self):
        self.ball()
        self.finished = False

    def ball(self):
        self.color = choice(COLORS)
        self.r = randint(10, 40)
        self.x = randint(self.r, WIDTH - self.r)
        self.y = randint(self.r, HEIGHT - self.r)
        self.vel = 100
        self.m_direction = random() * 2 * math.pi
        self.vel_x = self.vel * math.sin(self.m_direction)
        self.vel_y = self.vel * math.cos(self.m_direction)

    def IsMatchedBall(self, event):
        if (event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2 <= self.r ** 2:
            score.increase(1)
            self.ball()
        else:
            self.finished = True

    def movingball(self):
        if self.x > WIDTH - self.r:
            self.m_direction = randint(0, 360) / (2 * math.pi)
        elif self.x < self.r:
            self.m_direction = random() * math.pi
        if self.y > HEIGHT - self.r:
            self.m_direction = randint(0, 270) / (2 * math.pi)
        elif self.y < self.r:
            self.m_direction = randint(0, 90) / (2 * math.pi)
        self.vel_x = self.vel * math.sin(self.m_direction)
        self.vel_y = self.vel * math.cos(self.m_direction) * (-1)
        self.r = int(math.sin(pygame.time.get_ticks() / 600) * 1.5 + 20)
        self.x += self.vel_x / FPS
        self.y += self.vel_y / FPS
        circle(screen, self.color, (int(self.x), int(self.y)), self.r)


class Squarestrange(Ball):

    def IsMatchedBall2(self, event):
        if math.hypot(event.pos[0] - self.x, event.pos[1] - self.y) <= self.r:
            score.increase(2)
            self.ball()
        else:
            self.finished = True

    def movingsquarestrange(self):
        # if math.hypot(pos[0] - self.x, pos[1] - self.y) <= self.r:
        #     self.m_direction = random() * 2 * math.pi
        #     self.vel_x = self.vel * math.sin(self.m_direction)
        #     self.vel_y = self.vel * math.cos(self.m_direction)
        # else:
        #     if self.x > (WIDTH - self.r) or self.x < self.r:
        #         self.vel_x *= -1
        #     if self.y > (HEIGHT - self.r) or self.y < self.r:
        #         self.vel_y *= -1
        # self.x += self.vel_x / FPS
        # self.y += self.vel_y / FPS
        if self.x > WIDTH - self.r:
            self.m_direction = randint(0, 360) / (2 * math.pi)
        elif self.x < self.r:
            self.m_direction = random() * math.pi
        if self.y > HEIGHT - self.r:
            self.m_direction = randint(0, 270) / (2 * math.pi)
        elif self.y < self.r:
            self.m_direction = randint(0, 90) / (2 * math.pi)
        self.vel_x = self.vel * math.sin(self.m_direction)
        self.vel_y = self.vel * math.cos(self.m_direction) * (-1)
        self.r = int(math.sin(pygame.time.get_ticks() / 600) * 1.5 + 20)
        self.x += self.vel_x / FPS
        self.y += self.vel_y / FPS
        self.r = int(math.sin(pygame.time.get_ticks() / 100) * 6 + 20)
        rect(screen, choice(COLORS), [self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r], 15)


class Ghost(Ball):
    def __init__(self):
        super().__init__()
        self.subsurf = pygame.Surface((400, 600))

    def ghostparameters(self):
        self.color = choice(COLORS)
        self.r = randint(10, 40)
        self.x = randint(200, WIDTH - self.r - 200)
        self.y = randint(200, HEIGHT - self.r - 200)
        self.vel = 100
        self.m_direction = random() * 2 * math.pi
        self.vel_x = self.vel * math.sin(self.m_direction)
        self.vel_y = self.vel * math.cos(self.m_direction)

    def IsMatchedBall3(self, event):
        if math.hypot(event.pos[0] - int(self.x) - 55, event.pos[1] - int(self.y) - 60) <= 5 * self.r:
            score.increase(3)
            self.ghostparameters()
        else:
            self.finished = True

    def ghost(self, size=1):
        '''Drawing ghost, there sets screen, int(self.x), y, size'''
        circle(screen, MILDGREY, (int(self.x) + 75 * size, int(self.y) + 50 * size), 30 * size)
        circle(screen, CYAN, (int(self.x) + 63 * size, int(self.y) + 47 * size), 7 * size)
        circle(screen, WHITE, (int(self.x) + 63 * size, int(self.y) + 47 * size), 2 * size)
        circle(screen, CYAN, (int(self.x) + 82 * size, int(self.y) + 43 * size), 7 * size)
        circle(screen, WHITE, (int(self.x) + 82 * size, int(self.y) + 43 * size), 2 * size)
        polygon(screen, MILDGREY, ((int(self.x) + 75 * size, int(self.y) + 50 * size), (int(self.x) + 50 * size,
                                                                                        int(self.y) + 60 * size),
                                   (int(self.x) + 45 * size, int(self.y) + 90 * size), (int(self.x) + 60 * size,
                                                                                        int(self.y) + 130 * size),
                                   (int(self.x) + 40 * size, int(self.y) + 170 * size), (int(self.x) + 80 * size,
                                                                                         int(self.y) + 150 * size),
                                   (int(self.x) + 100 * size, int(self.y) + 165 * size), (int(self.x) + 125 * size,
                                                                                          int(self.y) + 145 * size),
                                   (int(self.x) + 140 * size, int(self.y) + 150 * size), (int(self.x) + 160 * size,
                                                                                          int(self.y) + 130 * size),
                                   (int(self.x) + 140 * size, int(self.y) + 100 * size), (int(self.x) + 120 * size,
                                                                                          int(self.y) + 80 * size),
                                   (int(self.x) + 105 * size, int(self.y) + 50 * size)))

    def movingghost(self):
        if self.x > WIDTH - self.r - 100:
            self.m_direction = randint(0, 360) / (2 * math.pi)
        elif self.x < self.r - 100:
            self.m_direction = random() * math.pi
        if self.y > HEIGHT - self.r - 250:
            self.m_direction = randint(0, 270) / (2 * math.pi)
        elif self.y < self.r + 50:
            self.m_direction = randint(0, 90) / (2 * math.pi)
        self.vel_x = self.vel * math.sin(self.m_direction)
        self.vel_y = self.vel * math.cos(self.m_direction) * (-1)
        self.r = int(math.sin(pygame.time.get_ticks() / 600) * 1.5 + 20)
        self.x += self.vel_x / FPS
        self.y += self.vel_y / FPS
        self.ghost()


class Score:
    def __init__(self):
        self.score = 0

    def increase(self, itt):
        self.score += itt

    def draw(self):
        subsurf_score = labelFont.render(str(self.score), False, BLUE)
        screen.blit(subsurf_score, (WIDTH / 2 - 50, 0))


balls = [Ball() for i in range(15)]
somes = [Squarestrange() for i in range(2)]
ghosts = [Ghost() for i in range(1)]
score = Score()
pygame.display.update()
clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)
    for ball in balls:
        ball.movingball()
    for squarestrange in somes:
        squarestrange.movingsquarestrange()
    for ghost in ghosts:
        ghost.movingghost()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                ball.IsMatchedBall(event)
            for squarestrange in somes:
                squarestrange.IsMatchedBall2(event)
            for ghost in ghosts:
                ghost.IsMatchedBall3(event)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons == (1, 0, 0):
                for ball in balls:
                    ball.IsMatchedBall(event)
                for squarestrange in somes:
                    squarestrange.IsMatchedBall2(event)
                for ghost in ghosts:
                    ghost.IsMatchedBall3(event)

    score.draw()
    pygame.display.update()
    screen.fill(WHITE)
output = (a)
output += ' scored '

output +=(str(score.score))
output +=('\n')

out.write(output)
out.close()
pygame.quit()
