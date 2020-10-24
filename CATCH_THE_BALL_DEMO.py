import pygame
from pygame.draw import *
from random import randint

FPS = 64

width = 1000
height = 750
info_width = 440
border_width = 8
upper_interval = 30
left_interval = 40
fontsize = 32
Points = 0
number_of_balls = 12
number_of_sq = 1

Game_Time = 30
HIT_time = 0


BorderColor = (0, 224, 0)
DigitsColor = (0, 255, 5)
WildBlue = (162, 173, 208)
BLUE = (0, 0, 255)
Honeydew = (240, 255, 240)
BlueViolet  = (138, 43, 226)
MAGENTA = (255, 0, 255)
PINK = (255, 105, 180)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
Gold = (255, 215, 0)
COLORS = [WildBlue, BLUE, Honeydew, BlueViolet, MAGENTA, PINK, CYAN]


# Парамтетры шаров
x = [randint(60 + border_width, 940 - border_width) 
    for i in range(number_of_balls)]
y = [randint(60 + border_width, 690 - border_width) 
    for i in range(number_of_balls)]
speed_x = [randint(-4, 4) for i in range(number_of_balls)]
speed_y = [randint(-4, 4) for i in range(number_of_balls)]
r = [randint(10, 60) for i in range(number_of_balls)]
color_number = [randint(0, 6) for i in range(number_of_balls)]

# Параметры квадратов
x_sq = [randint(border_width, 950 - border_width) 
        for i in range(number_of_sq)]
y_sq = [randint(border_width, 700 - border_width) 
        for i in range(number_of_sq)]
speed_sq_x = [randint(5, 8) for i in range(number_of_sq)]
speed_sq_y = [randint(5, 8) for i in range(number_of_sq)]
a = [randint(20, 50) for i in range(number_of_sq)]


def digits(inf:str, x, y, fs_local):
    font = pygame.font.SysFont('Arial', fs_local)
    inform = font.render(str(inf), 1, DigitsColor)
    screen.blit(inform, (x, y) )
        

def new_ball(f:int):
    '''Функция рисующая шарик'''
    circle(screen, COLORS[color_number[f]], (x[f], y[f]), r[f])


def sq(f:int):
    '''Функция для квадрата'''
    rect(screen, Gold, (x_sq[f], y_sq[f], a[f], a[f]))


def click(event):
    '''Функция начисления очков'''
    global Points, HIT_time
    for i in range(number_of_balls):
        if (event.pos[0]-x[i])**2+(event.pos[1]-y[i])**2 <= r[i]**2:

            Points += 500*((speed_x[i]**2 + speed_y[i]**2)**0.5)/r[i]**2

            x[i] = randint(80 + border_width, 
                    920 - border_width)
            y[i] = randint(80 + border_width, 
                    670 - border_width)
            speed_x[i] = randint(-4, 4)
            speed_y[i] = randint(-4, 4)
            r[i] = randint(10, 60)
            color_number[i] = randint(0, 6)


    for i in range(number_of_sq):
        if ((x_sq[i] <= event.pos[0] <= x_sq[i] + a[i]) and 
            (y_sq[i] <= event.pos[1] <= y_sq[i] + a[i])):

            HIT_time = 1      
      
            Points += (2500 * ((speed_sq_x[i]**2 + 
                    speed_sq_y[i]**2)**0.5)/a[i]**2)

            x_sq[i] = randint(border_width,
                     950 - border_width)
            y_sq[i] = randint(border_width,
                     700 - border_width)
            speed_sq_x[i] = randint(5, 8)
            speed_sq_y[i] = randint(5, 8)
            a[i] = randint(20, 50)
            

        elif ((x_sq[i] - 50 <= event.pos[0] <= x_sq[i] + a[i] + 50) and 
            (y_sq[i] - 50 <= event.pos[1] <= y_sq[i] + a[i] + 50)):

            if randint(0, 1):
                speed_sq_x[i] *= -1
            else:
                speed_sq_y[i] *= -1

# Создает список с лучшими результатами
with open('List_of_scores.txt', 'r') as file:
    list_for_sort = []
    for f, line in enumerate(file):
        if f > 1:
            element = line[line.find(' ')+1:]
            list_for_sort.append(
            int(element.rstrip()))
list_for_sort.sort(reverse=True)               


pygame.init()

screen = pygame.display.set_mode((width + info_width, height))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    t = round(pygame.time.get_ticks()/1000, 1)
    Points = round(Points, 1)

    # Прорисовывает контур 
    rect(screen, BorderColor, (0, 0 , width + info_width, height),
         border_width)
    rect(screen, BorderColor, (0, 0 , width, height), border_width)
    rect(screen, BorderColor, (width, 0, info_width, 
            3*upper_interval + 2*fontsize), border_width)

    # Выволит время на экран
    digits('Time: ' + str(t), width + left_interval, 
            2*upper_interval + fontsize, fontsize)

    # Выводит счет игрока на экран
    digits('Points: ' + str(Points), width + left_interval,
             upper_interval, fontsize)

    # Вводит надпсиь 'Best Scores'
    digits('Best Scores ', width + left_interval, 
            4*upper_interval + 2*fontsize, fontsize)
    
    # Выводит таблицу лучших результатов
    n = 1
    for i in list_for_sort[:8]:
        digits(str(n) + ': ' + str(i), width + left_interval,
            (4+n)*upper_interval + 
            (2+n)*fontsize, fontsize)
        n += 1

    # Проверяет, чтоб скорость шаров была больше нуля
    for i in range(number_of_balls):
        if speed_x[i] == 0:
            speed_x[i] += 1
        if speed_y[i] == 0:
            speed_y[i] += 1

    # Рисует все шарики каждый кадр и проверяет их положение
    for i in range(number_of_balls):
        new_ball(i)

        if ((x[i] < width - r[i] - border_width) and
            (x[i] > r[i] + border_width)):
            x[i] += speed_x[i]
        else:
            speed_x[i] *= -1
            x[i] += speed_x[i]

        if ((y[i] < height - r[i] - border_width) and
             (y[i] > r[i] + border_width)):
            y[i] += speed_y[i]
        else:
            speed_y[i] *= -1
            y[i] += speed_y[i]

    # Прорисовывает движение квадратов
    for i in range(number_of_sq):
        sq(i)

        if ((x_sq[i] > border_width) and 
            (x_sq[i] < width - a[i] - border_width)):
            x_sq[i] += speed_sq_x[i]
        else:
            speed_sq_x[i] *= -1
            x_sq[i] += speed_sq_x[i]

        if ((y_sq[i] > border_width) and 
            (y_sq[i] < height - a[i] - border_width)):
            y_sq[i] += speed_sq_y[i]
        else:
            speed_sq_y[i] *= -1
            y_sq[i] += speed_sq_y[i]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('List_of_scores.txt', 'r') as file:
                nstrings = 0
                for line in file:
                    nstrings += 1
            nstrings -= 1
            with open('List_of_scores.txt', 'a') as file:
                file.write('\n' + str(nstrings) + ': ' +
                            str(int(100 * round(Points/t, 2))))
            print('Вас счет - ' + str(Points))
            print(t, 'c')
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    # Выводит YEAH! на экран при попадании по квадрату
    if HIT_time > 0:
        digits('YEAH!', width//3, height//2 - width//6 , width//6)
    

    HIT_time -= 1/FPS

    
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()