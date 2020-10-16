import pygame
from pygame.draw import *
from random import randint, choice, random
import math
pygame.init()
pygame.font.init()

FPS = 60
WIDTH = 1200
HEIGHT = 800
Score_size = 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
labelFont = pygame.font.SysFont('Helvetic', Score_size)

WHITE = (255, 255, 255)
MILDERGREY = (190, 190, 190)
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

    def movingsquarestrange(self, pos):
        if math.hypot(pos[0] - self.x, pos[1] - self.y) <= self.r:
            self.m_direction = random() * 2 * math.pi
            self.vel_x = self.vel * math.sin(self.m_direction)
            self.vel_y = self.vel * math.cos(self.m_direction)
        else:
            if self.x > (WIDTH - self.r) or self.x < self.r:
                self.vel_x *= -1
            if self.y > (HEIGHT - self.r) or self.y < self.r:
                self.vel_y *= -1
        self.x += self.vel_x / FPS
        self.y += self.vel_y / FPS
        self.r = int(math.sin(pygame.time.get_ticks() / 100) * 6 + 20)
        rect(screen, choice(COLORS), [self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r], 15)


class Score:
    def __init__(self):
        self.score = 0

    def increase(self, itt):
        self.score += itt

    def draw(self):
        subsurf_score = labelFont.render(str(self.score), False, BLUE)
        screen.blit(subsurf_score, (WIDTH / 2 - 50, 0))


balls = [Ball() for i in range(20)]
somes = [Squarestrange() for i in range(10)]
score = Score()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for ball in balls:
        ball.movingball()
    for squarestrange in somes:
        squarestrange.movingsquarestrange(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                ball.IsMatchedBall(event)
            for squarestrange in somes:
                squarestrange.IsMatchedBall2(event)
    score.draw()
    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
