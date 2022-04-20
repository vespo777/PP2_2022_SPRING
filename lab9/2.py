from os import scandir
from select import select
import pygame
import random
import sys
import time
import datetime

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE= (0, 0, 255)
RED= (255, 0, 255) 
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
cnt=0

SCORE=0
LEVEL=0

BLOCK_SIZE = 20



score_font = pygame.font.SysFont('Verdana', 72)




class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Food:
    def __init__(self):
        self.location = Point(random.randint(0,  19), random.randint(0,  19))

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def respawn(self):
        self.location.x = random.randint(0,  19)
        self.location.y = random.randint(0,  19)



class Snake:
    def __init__(self):
        self.body = [Point(random.randint(0,  19), random.randint(0,  19))]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 


        if self.body[0].x * BLOCK_SIZE > WIDTH:
            #self.body[0].x = 0
            SCREEN.fill(RED)
            pygame.quit()
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            #self.body[0].y = 0
            SCREEN.fill(RED)
            pygame.quit()

        if self.body[0].x < 0:
            #self.body[0].x = WIDTH / BLOCK_SIZE
            SCREEN.fill(RED)
            pygame.quit()
        
        if self.body[0].y < 0:
            #self.body[0].y = HEIGHT / BLOCK_SIZE
            SCREEN.fill(RED)
            pygame.quit()

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect( SCREEN, (255, 0, 0), rect)



        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect( SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):
        global SCORE
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                SCORE+=random.randint(1, 3)
                food.respawn()

    def timer(self, food):
        global cnt, start
        seconds = time.time()
        if cnt==0:
            start= seconds
            cnt+=1
        print("Time in seconds:", seconds-start)
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                start=seconds
        if seconds-start>=10:
            food.respawn()
            start=seconds
        



def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
        
        snake.move()

        snake.check_collision(food)
        snake.timer(food)

        score_img = score_font.render( str(SCORE), True, WHITE)

        SCREEN.fill(BLACK)
        SCREEN.blit(score_img, (10, 10) )


        
        snake.draw()
        food.draw()

        
        drawGrid()

        pygame.display.update()
        pygame.display.flip()
        if SCORE>2:
            CLOCK.tick(10)
        else:
            CLOCK.tick(5)



def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


main()