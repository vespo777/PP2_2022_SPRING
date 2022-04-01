import pygame

pygame.init()
fps=30
fpsclock=pygame.time.Clock()
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Keyboard_Input")
White=(255,255,255)
p1=350
p2=350
step=20
while True:
    screen.fill(White)
    pygame.draw.circle(screen, (255,0,0), (p1, p2) , 25)
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        if p1-step>=25 :
            p1 -= step
    if key_input[pygame.K_UP]:
        if p2-step>=25:
            p2 -= step
    if key_input[pygame.K_RIGHT]:
        if p1+step<675:
            p1 += step
    if key_input[pygame.K_DOWN]:
        if p2+step<675:
            p2 += step
    pygame.display.update()
    fpsclock.tick(fps)
