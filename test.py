import random, sys, os
os.environ["DISPLAY"] = ":0"
sys.path.insert(0,"/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car")
from graphic import camera
from graphic import maps
import pygame
import graphic.stone as stone
import graphic.traffic_lamp as traffic_lamp
from pygame.locals import *
import time

from graphic import car
from graphic.car import calculate_angle

gameDisplay = pygame.display.set_mode((1200, 600))
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (40,250,20)
bright_red = (255,50,50)
bright_green = (100,250,90)
block_color = (53,115,255)
display_width = 1200
display_height = 600
clock = pygame.time.Clock()
intro = True
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    global intro
    intro = True
    bg = pygame.image.load("/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/map_ldh_940_640.png")
    #INSIDE OF THE GAME LOOP
    while intro:
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Autonomous vehicle", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Test",500,450,100,50,green,bright_green,action='map7')
        RADIUS = 20
        ZEROINTENSITY = 0
        MAXINTENSITY = 255
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                COLOR = (random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY), random.randint(ZEROINTENSITY, MAXINTENSITY))
                #note- we have skipped the last parameter and by default, 0 is taken
                pygame.draw.circle(screen, COLOR, pos, RADIUS)


        pygame.display.update()
        clock.tick(15)
        
def button(msg,x,y,w,h,ic,ac,action=None):
    global intro
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(mouse)
    # print("----")
    # print(click)
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'quit':
                intro = False
            else:
                # print("hihi")
                main_mapx(int(action[3:]))
                
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    # print(mouse)
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def main():
    game_intro()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1200, 640))
    
    pygame.display.set_caption("BTL_XLTTM")
    pygame.mouse.set_visible(True)
    font = pygame.font.Font(None, 24)

    CENTER_W = int(pygame.display.Info().current_w / 2)
    CENTER_H = int(pygame.display.Info().current_h / 2)
    

    # new background surface
    background = pygame.Surface(screen.get_size())
    background = background.convert_alpha(background)
    background.fill((82, 86, 94))

    # main loop
    main()

    pygame.quit()
    sys.exit(0)
