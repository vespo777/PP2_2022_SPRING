import random
import sys
import pygame


FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMTY_STEP = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCORE  = 0
SCORE_COIN  = 0


clock = pygame.time.Clock()


pygame.init()

score_font = pygame.font.SysFont("Verdana", 20)
score_coin_font = pygame.font.SysFont("Verdana", 20)

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

bg = pygame.image.load(r"C:\Users\tileu\Desktop\istok\AnimatedStreet.png")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\tileu\Desktop\istok\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE+=1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\tileu\Desktop\istok\Coin16.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(70, SCREEN_WIDTH - 70), random.randint(70, SCREEN_WIDTH - 70))

    def update(self):
        global SCORE_COIN, ENEMTY_STEP
        if pygame.sprite.spritecollideany(P1, coin):
            SCORE_COIN+=random.randint(1, 3) #добавляет случайное количество баллов к счету 
            if SCORE_COIN%10==0:
                ENEMTY_STEP+=3 #добавляет скорость противника
            self.rect.center = (random.randint(70, 330), random.randint(70, 530))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\tileu\Desktop\istok\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 300)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
        
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -STEP)

        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, STEP)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C1 = Coin()

#что бы добавить классы игрока и врага в одну группу
enemies = pygame.sprite.Group()
enemies.add(E1)
coin = pygame.sprite.Group()
coin.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #When racer collide on enemy, and in this moment happen Game Over
    if pygame.sprite.spritecollideany(P1, enemies):
          SURF.fill(RED)
          pygame.quit()
          sys.exit()

        


    P1.update()
    E1.update()
    C1.update()

    SURF.blit(bg, (0, 0))

    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)

    score_img = score_font.render(str(SCORE), True, BLACK)
    SURF.blit(score_img, (10, 10))
    #Счет
    score_coin_img = score_font.render(str(SCORE_COIN), True, BLACK)
    SURF.blit(score_coin_img, (100, 10))
    

    pygame.display.update()
    clock.tick(FPS)