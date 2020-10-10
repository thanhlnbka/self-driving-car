import random, sys, os
# os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["DISPLAY"] = ":0"
sys.path.insert(0,"/home/luuthanh/Desktop/fuzzy-logic-project/")
from graphic import camera
from graphic import maps
import pygame
import graphic.stone as stone
import graphic.traffic_lamp as traffic_lamp
from pygame.locals import *

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
def button(msg,x,y,w,h,ic,ac,action=None):
    global intro
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == 'quit':
                intro = False
            else:
                # print(action)
                main_mapx(int(action[3:])+2)
                
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def game_intro():
    global intro
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Self Driving Car", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Map 1",100,450,100,50,green,bright_green,action='map1')
        button("Map 2",300,450,100,50,green,bright_green,action='map2')
        button("Map 3",500,450,100,50,green,bright_green,action='map3')
        button("Map 4",700,450,100,50,green,bright_green,action='map4')
        button("Quit",900,450,100,50,red,bright_red,'quit')

        pygame.display.update()
        clock.tick(15)

def main_mapx(x):

    clock = pygame.time.Clock()
    running = True
    one_time = True
    cam = camera.Camera()
    # traffic_lamp1 = traffic_lamp.TrafficLamp(1610, 420, 90, 0)
    # traffic_lamp2 = traffic_lamp.TrafficLamp(2710, 1520, 90, 1)

    stone_impediment = stone.Stone(1200, 800, 90, 0)
    
    map_s = pygame.sprite.Group()
    map_s.add(maps.Map(0, 0, x))
    start_x = maps.MAP_NAVS[0][0]
    start_y = maps.MAP_NAVS[0][1]
    # print(maps.MAP_NAVS)
    maps.FINISH_INDEX = len(maps.MAP_NAVS) - 2

    traffic_lamp1 = traffic_lamp.TrafficLamp(maps.TRAFFIC_LAMP_COORDINATES[0])
    traffic_lamp2 = traffic_lamp.TrafficLamp(maps.TRAFFIC_LAMP_COORDINATES[1])

#     print(maps.TRAFFIC_LAMP_COORDINATES[0])
#     print(maps.TRAFFIC_LAMP_COORDINATES[1])

    start_angle = calculate_angle(maps.MAP_NAVS[0][0],
                                  maps.MAP_NAVS[0][1], maps.MAP_NAVS[1][0], maps.MAP_NAVS[1][1])
    # print("Start angle: ", start_angle)
    # print("Finish index: ", maps.FINISH_INDEX)

    controlled_car = car.Car(start_x, start_y, start_angle,x)
    cars = pygame.sprite.Group()
    cars.add(controlled_car)
    print(cars)
    traffic_lamps = pygame.sprite.Group()
    traffic_lamps.add(traffic_lamp1)
    traffic_lamps.add(traffic_lamp2)

    stones = pygame.sprite.Group()
    stones.add(stone_impediment)

    stone_status = (stone_impediment.status, len(maps.MAP_NAVS) - 1)

    cam.set_pos(controlled_car.x, controlled_car.y)
    flag = 0
    pause = False 
    while running:
        
        flag += 1
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
#             print("event.type+ ",event.type)
#             print(keys)
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYUP:
                if keys[K_p]:
                    pause = True
                if keys[K_s]:
                    pause = False
                if keys[K_q]:
#                     pygame.quit()
#                     sys.exit(0)
                    map_s.empty()
                    maps.MAP_NAVS = []
                    maps.FINISH_INDEX = 0
                    maps.TRAFFIC_LAMP_POS = []
                    maps.TRAFFIC_LAMP_COORDINATES = []
                    cars.empty()
                    # return
                    running=False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break

            # mouse event
        
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_p:
#                     pause = True
#                     paused()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                if pressed1:
                    print("left click")
                    current_index = controlled_car.current_nav_index
                    random_index = random.randrange(current_index + 3, current_index + 10)
                    if random_index <= (len(maps.MAP_NAVS) - 3) and stone_impediment.status == 0:
                        x = maps.MAP_NAVS[random_index][0]
                        y = maps.MAP_NAVS[random_index][1]
                        stone_impediment.switch_status(x, y)
                        stone_status = (stone_impediment.status, random_index)
                    else:
                        stone_impediment.switch_status(0, 0)
                        stone_status = (0, len(maps.MAP_NAVS) - 1)
        # print(controlled_car.x, controlled_car.y)
        cam.set_pos(controlled_car.x, controlled_car.y)

        screen.blit(background, (0, 0))

        # update and render map
        map_s.update(cam.x, cam.y)
        map_s.draw(screen)

        # update and render traffic lamps
        traffic_lamps_status = []
        traffic_lamps.update(cam.x, cam.y)
        traffic_lamps.draw(screen)

        stones.update(cam.x, cam.y)
        stones.draw(screen)

        # for lamp in traffic_lamps:
        #     lamp_status = lamp.render(screen)
        #     traffic_lamps_status.append(lamp_status)
        lamp_status1 = traffic_lamp1.render(screen)
        lamp_status2 = traffic_lamp2.render(screen)

        traffic_lamps_status.append(lamp_status1)
        traffic_lamps_status.append(lamp_status2)
        # update and render car
        check = cars.update(cam.x, cam.y, traffic_lamps_status, stone_status, flag,pause)
        
            
        # print('check==================',check)
        cars.draw(screen)

        pygame.display.flip()
#         if check and one_time:
#             one_time = False
#             break
#         if controlled_car.current_nav_index == maps.FINISH_INDEX:
#             break
        clock.tick(60)

def main():
    game_intro()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Self Driving Car")
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