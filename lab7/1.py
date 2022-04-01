import pygame
from datetime import datetime
import math

pygame.init()
surface = pygame.display.set_mode((595, 600))
clock = pygame.time.Clock()

def change_image(image, t):
    im_rotate = pygame.transform.rotate(image,360 - t*6 )
    return im_rotate
main = pygame.image.load(r"C:\Users\tileu\Desktop\istok\main.jpg")
mmm = pygame.image.load(r"C:\Users\tileu\Desktop\istok\mmm.png")
sss = pygame.image.load(r"C:\Users\tileu\Desktop\istok\sss.png")


def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)



angle_for_min = 360
angle_for_sec = 360

t = datetime.now()

minute, second =  t.minute, t.second
minutes = change_image(mmm, minute)
secund = change_image(sss, second)
while True:
    surface.blit(main, (0, 0))
    w, h = secund.get_size()
    w1, h1 = minutes.get_size()
    blitRotate(surface, secund, (297.5, 300), (w/2, h/2), angle_for_sec)
    blitRotate(surface, minutes, (297.5, 300), (w1/2, h1/2), angle_for_min)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    angle_for_sec-=6
    angle_for_min-= 1/10
    pygame.display.flip()
    clock.tick(1)