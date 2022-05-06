import pygame
import random
from connect import insert, update, select, connection

name = input()
pygame.init()
WIDTH = 400
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

FPS = 10
BLOCK = 20
LENGTH = 1
level = 1
score = 0
CLOCK = pygame.time.Clock()
START = pygame.font.SysFont('Verdana',50)
FINISH = pygame.font.SysFont('Verdana',50)
SCORE = pygame.font.SysFont('Verdana',15)
LEVEL = pygame.font.SysFont('Verdana',15)
PAUSE = pygame.font.SysFont('Verdana',50)
pause_render = PAUSE.render('PAUSE',True,'yellow')
pause_rect = pause_render.get_rect(center=(WIDTH//2,HEIGHT//2))

def Wall(LEVEL):
    f = open(f'C:\python\lab10\level1.txt{LEVEL}.txt','r')
    for x in range(0, WIDTH+1, BLOCK):
        for y in range(0, HEIGHT+1, BLOCK):
            if f.read(1) == '#':
                pygame.draw.rect(SCREEN, 'chocolate', (y, x, BLOCK, BLOCK))

def walls(LEVEL):
    f = open(f'C:\python\lab10\level1.txt{LEVEL}.txt','r')
    WALLS = []
    for x in range(0, WIDTH+1, BLOCK):
        for y in range(0, HEIGHT+1, BLOCK):
            if f.read(1) == '#':
                WALLS.append((y,x))
    return WALLS

def points(LEVEL):
    POINTS = []
    f = open(f'C:\python\lab10\level1.txt{LEVEL}.txt','r')
    for x in range(0, WIDTH+1, BLOCK):
        for y in range(0, HEIGHT+1, BLOCK):
            if f.read(1) == '.':
                POINTS.append((y,x))
    return POINTS

def lines():
    for x in range(0, WIDTH+1, BLOCK):
        for y in range(0, HEIGHT+1, BLOCK):
            pygame.draw.rect(SCREEN,'indigo',(x, y, BLOCK, BLOCK),1)

x,y = random.choice(points(level))
apple = random.choice(points(level))
dx,dy = 0,0
snake = [(x,y)]
dirs = {'Up':True, 'Down':True, 'Right':True, 'Left':True}
done = True
pause, running = 0, 1
state = running
s = 0

cnt = 0 
for sub in select:
    if name in sub:
        cnt += 1

if cnt == 0:
    insert(connection, f"'{name}'", score)
 
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                s += 1
            if s%2 == 0:
                state = running
            else:
                state = pause
        
    if state == running:
        SCREEN.fill('black')

        update(connection, f"'{name}'", score)

        while done:

            render_start = START.render('TAP TO START', True, 'darkgreen')
            rect_start = render_start.get_rect(center=(WIDTH//2,HEIGHT//2))
            SCREEN.blit(render_start,rect_start)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = False
        
        #drawing walls,lines
        Wall(level)
        lines()
        

        snake.append((x,y))
        snake = snake[-LENGTH:]

        #game over
        for i in snake:
            for j in walls(level):
                if i == j:
                    finish_render = FINISH.render('GAME OVER', True, 'Yellow')
                    finish_rect = finish_render.get_rect(center = (WIDTH//2, HEIGHT//2))
                    SCREEN.blit(finish_render,finish_rect)
                    pygame.display.flip()

                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                connection.close()
                                exit()

        if x>WIDTH-BLOCK or x<0 or y>HEIGHT-BLOCK or y<0 or len(snake)>len(set(snake)):
            finish_render = FINISH.render('GAME OVER', True, 'Yellow')
            finish_rect = finish_render.get_rect(center = (WIDTH//2, HEIGHT//2))
            SCREEN.blit(finish_render,finish_rect)
            pygame.display.flip()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        connection.close()
                        exit()

        #drawing snake,apple
        for i,j in snake:
            pygame.draw.rect(SCREEN, 'green', (i, j, BLOCK-1, BLOCK-1))
        pygame.draw.rect(SCREEN, 'red', (*apple, BLOCK, BLOCK))

        level_render = LEVEL.render(f'LEVEL:{level}', True , 'yellow')
        score_render = SCORE.render(f'SCORE:{score}', True, 'yellow')

        SCREEN.blit(level_render,(0,0))
        SCREEN.blit(score_render,(0,20))

        pygame.display.flip()
        CLOCK.tick(FPS)

        #eating apple
        if snake[-1] == apple:
            score += 1
            if score%4 == 0:
                level += 1
                FPS += 1

            LENGTH += 1
            apple = random.choice(points(level))
            
        #snake move
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and dirs['Up']:
            dx,dy = 0,-1
            dirs = {'Up':True, 'Down':False, 'Right':True, 'Left':True}
        if pressed[pygame.K_DOWN] and dirs['Down']:
            dx,dy = 0,1
            dirs = {'Up':False, 'Down':True, 'Right':True, 'Left':True}
        if pressed[pygame.K_RIGHT] and dirs['Right']:
            dx,dy = 1,0
            dirs = {'Up':True, 'Down':True, 'Right':True, 'Left':False}
        if pressed[pygame.K_LEFT] and dirs['Left']:
            dx,dy = -1,0
            dirs = {'Up':True, 'Down':True, 'Right':False, 'Left':True}
        
        if pressed[pygame.K_p]:
            pause = True


        x += dx*BLOCK
        y += dy*BLOCK

    elif state == pause:
        SCREEN.blit(pause_render,pause_rect)
        pygame.display.flip()