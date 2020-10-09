import pygame
from pygame.draw import *
from random import randint as ri

# Б-02-010
# Дашиев Максим

width = 900
height = 600

pygame.init()

FPS = 30
screen = pygame.display.set_mode((width, height))


# Функция для рисования человека
def big_man(x, y):
	'''
	Функция рисующая людей.
	На вход принимается местположние 
	человека (В коорд x и y).
	'''
	ellipse(screen, (145,124,111), (35+x, 40+y, 70, 60))
	rect(screen, (145,124,111), (35+x, 70+y, 70, 60))
	rect(screen, (108,93,83), (63+x, 60+y, 15, 70))
	ellipse(screen, (227,222,219), (40+x, 20+y, 60, 40))
	ellipse(screen, (145,124,111), (50+x, 25+y, 40, 30))
	ellipse(screen, (227,219,219), (58+x, 28+y, 25, 25))
	aalines(screen, (0,0,0),False,
			[[65+x, 48+y], [70+x, 47+y], [75+x, 48+y]])
	aalines(screen,(0,0,0),False,
			[[63+x, 35+y], [68+x, 38+y]])
	aalines(screen,(0,0,0),False,
			[[72+x, 38+y], [77+x, 35+y]])
	polygon(screen, (0, 0, 0), [(10+x,130+y), (10+x,0+y)], 1)
	ellipse(screen, (145,124,111), (0+x, 55+y, 50, 20))
	ellipse(screen, (145,124,111), (90+x, 55+y, 50, 20))
	ellipse(screen, (145,124,111), (35+x, 100+y, 25, 50))
	ellipse(screen, (145,124,111), (80+x, 100+y, 25, 50))
	ellipse(screen, (145,124,111), (25+x, 140+y, 30, 10))
	ellipse(screen, (145,124,111), (85+x, 140+y, 30, 10))
	rect(screen, (108,93,83), (35+x, 115+y, 70, 15))


def home(x, y):
	'''
	Функция рисующая жилище.
	Входные данные - это координаты 
	жилища.
	'''
	arc(screen,(0, 0, 0) , (0+x, 0+y, 170, 170), 0.05, 3.1, 5)
	polygon(screen, (0, 0, 0), [(0+x, 80+y), (170+x, 80+y)],1)
	polygon(screen, (0, 0, 0), [(10+x, 60+y), (160+x, 60+y)],1)
	polygon(screen, (0, 0, 0), [(15+x, 40+y), (155+x, 40+y)],1)
	polygon(screen, (0, 0, 0), [(30+x, 20+y), (140+x, 20+y)],1)
	polygon(screen, (0, 0, 0), [(30+x, 80+y), (30+x, 20+y)],1)
	polygon(screen, (0, 0, 0), [(140+x, 80+y), (140+x, 20+y)],1)
	polygon(screen, (0, 0, 0), [(60+x, 80+y), (60+x, 10+y)],1)
	polygon(screen, (0, 0, 0), [(110+x, 80+y), (110+x, 10+y)],1)
	polygon(screen, (0, 0, 0), [(85+x, 80+y), (85+x, 0+y)],1)


def pet(x, y):
	'''
	Функция рисующая зверька.
	Входные данные - это координаты 
	зверька.
	'''
	ellipse(screen,(204,204,204), (13+x, 10+y, 80, 30)) 
	ellipse(screen,(204,204,204), (3+x, 0+y, 25, 25)) 
	rect(screen, (204,204,204), (5+x, 1+y, 10, 10)) 
	rect(screen, (204,204,204), (15+x, 1+y, 10, 10)) 
	ellipse(screen,(255,255,255), (5+x, 6+y, 7, 5)) 
	ellipse(screen,(0,0,0), (9+x, 7+y, 4, 4)) 
	ellipse(screen,(255,255,255), (15+x, 6+y, 7, 5)) 
	ellipse(screen,(0,0,0), (18+x, 7+y, 4, 4)) 
	ellipse(screen,(0,0,0), (12+x, 13+y, 4, 2)) 
	ellipse(screen,(204,204,204), (73+x, 15+y, 15, 40)) 
	ellipse(screen,(204,204,204), (69+x, 50+y, 15, 10)) 
	ellipse(screen,(204,204,204), (18+x, 15+y, 15, 40)) 
	ellipse(screen,(204,204,204), (13+x, 50+y, 15, 10)) 
	ellipse(screen,(204,204,204), (78+x, 15+y, 50, 10)) 
	rect(screen, (211,95,95), (7+x, 14+y, 18, 11)) 
	ellipse(screen,(147,172,167),(0+x, 15+y, 30, 10)) 
	rect(screen, (147,172,167), (29+x, 16+y, 8, 8)) 
	ellipse(screen,(29,34,238),(3+x, 18+y, 5, 5)) 
	ellipse(screen,(255,255,255), (8+x, 15+y, 3, 6)) 
	ellipse(screen,(255,255,255), (19+x, 15+y, 3, 6)) 


# Фоновая заливка
rect(screen, (255, 255, 255), (0, (3*height)//4, width, height//4))
rect(screen, (249,249,249), (0, height//2, width, height//4))
rect(screen, (230,230,230), (0, 0, width, height//2))


# Дома
for i in range(5):
	home(width//20 + width//5 * i - (i//3) * width//2, 
		 height//3 + (i//3)*height//8)

# Люди
for i in range(5):
	big_man(2*width//5 + ri(23, 27)*width//120 * i - (i//3) * width//2, 
		 	height//2 + (i//3)*height//6)

# Зверьки
for i in range(6):
	pet(-width//20 + width//5 * i, 
		 2*height//3 + ri(9, 14)*height//76)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()