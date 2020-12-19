import pygame
import sys
import os
import random
os.environ["DISPLAY"] = ":0"

#initialize pygame
pygame.init()


screen = pygame.display.set_mode([1200,600])

#caption for the game
pygame.display.set_caption("My first game in pygame")
RADIUS = 20
ZEROINTENSITY = 0
MAXINTENSITY = 255
bg = pygame.image.load("/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/map_ldh_940_640.png")
#INSIDE OF THE GAME LOOP
screen.blit(bg, (0, 0))
toado = []
while True:
    pos = pygame.mouse.get_pos()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Here for any commands inside the for loop  
        if events.type == pygame.MOUSEBUTTONDOWN:
            COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if len(toado) <=2 :
                toado.append(pos)
                pygame.draw.circle(screen, COLOR, pos, 20)
    print(toado)
    pygame.display.update()
