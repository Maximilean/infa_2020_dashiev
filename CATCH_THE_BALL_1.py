import pygame
from pygame.draw import *
from random import randint

FPS = 64

width = 1000
height = 750

score = 0
number_of_balls = 12

ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
PINK = (255, 105, 180)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [ORANGE, BLUE, YELLOW, GREEN, MAGENTA, CYAN, PINK]


x = [randint(80, 920) for i in range(number_of_balls)]
y = [randint(80, 670) for i in range(number_of_balls)]
speed_x = [randint(-4, 4) for i in range(number_of_balls)]
speed_y = [randint(-4, 4) for i in range(number_of_balls)]
r = [randint(10, 60) for i in range(number_of_balls)]
color_number = [randint(0, 6) for i in range(number_of_balls)]


def new_ball(f:int):
    '''Функция рисующая шарик'''
    circle(screen, COLORS[color_number[f]], (x[f], y[f]), r[f])


def click(event):
    '''Функция начисления очков'''
    global score
    for i in range(number_of_balls):
        if (event.pos[0]-x[i])**2+(event.pos[1]-y[i])**2 <= r[i]**2:
            x[i] = randint(80, 920)
            y[i] = randint(80, 670)
            speed_x[i] = randint(-4, 4)
            speed_y[i] = randint(-4, 4)
            r[i] = randint(10, 60)
            color_number[i] = randint(0, 6)

            score += 500*((speed_x[i]**2 + speed_y[i]**2)**0.5)/r[i]**2


pygame.init()

screen = pygame.display.set_mode((width, height))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    # Рисует все шарики каждый кадр и проверяет их положение

    for i in range(number_of_balls):
        new_ball(i)

        if (x[i] < width - r[i]) and (x[i] > r[i]):
            x[i] += speed_x[i]
        else:
            speed_x[i] *= -1
            x[i] += speed_x[i]

        if (y[i] < height - r[i]) and (y[i] > r[i]):
            y[i] += speed_y[i]
        else:
            speed_y[i] *= -1
            y[i] += speed_y[i]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Вас счет - ' + str(round(score, 1)))
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()