from turtle import position
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    mode = 'pen'
    baseLayer = pygame.Surface((800, 600))

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
    color = (255, 255, 255)
    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mode = "rect"
                elif event.key == pygame.K_DOWN:
                    mode = "circ"
                elif event.key == pygame.K_l:
                    mode = 'line'
                elif event.key == pygame.K_e:
                    mode = 'eras'
                elif event.key == pygame.K_r:
                    color = (255, 0 , 0 )
                elif event.key == pygame.K_g:
                    color = (0 , 255 , 0 )
                elif event.key == pygame.K_b:
                    color = (0, 0 , 255 )
                elif event.key == pygame.K_q:
                    mode = 'eras.r'
            if mode == "rect":
                if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                    screen.blit(baseLayer, (0, 0))
                    r = calculateRect(prevX, prevY, currentX, currentY)
                    pygame.draw.rect(screen, color,pygame.Rect(r), 1)

            elif mode == 'line':
                if isMouseDown:
                    pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))
                prevX = currentX
                prevY = currentY

            elif mode == "circ":
                if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                    screen.blit(baseLayer, (0, 0))
                    r = calculateRect(prevX, prevY, currentX, currentY)
                    pygame.draw.circle(screen, color,( (prevX+currentX)/2, (prevY+currentY)/2 ), ( (currentX-prevX)**2 + (currentY-prevY)**2  )**0.5 / 2,   1)

            elif mode == "eras":
                if isMouseDown:
                    pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY),10)
                prevX = currentX
                prevY = currentY
            
            elif mode == "eras.r":
                if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                    pygame.draw.rect(screen, pygame.Color('black'), (prevX, prevY, abs(currentX - prevX), abs(currentY - prevY)))


        pygame.display.flip()
        clock.tick(60)
        
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

main()