import pygame
import xlrd

from graphic.loader import load_image

# Map filenames.
MAP_NAVS = []
# MAP_NAVS = [(288, 594), (130, 593), (63, 593), (64, 178), (231, 177), (231, 26)]

FINISH_INDEX = 0

TRAFFIC_LAMP_POS = []
TRAFFIC_LAMP_COORDINATES = []


class Map(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, map_number):
        pygame.sprite.Sprite.__init__(self)
        self.map_number = map_number
        image_temp = "map"+str(map_number)   + ".png"
        self.get_map_navs()
        self.image = load_image(image_temp)
        
        self.rect = self.image.get_rect()
        self.x = init_x
        self.y = init_y

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x + 600, self.y - cam_y + 300

    def get_map_navs(self):
        with xlrd.open_workbook('/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/abc.xlsx') as book:
            sheet = book.sheet_by_name('Map0'+str(self.map_number))
            x_coordinate = [x for x in sheet.col_values(1)]
            y_coordinate = [y for y in sheet.col_values(2)]
            for i in range(1, len(x_coordinate)):
                MAP_NAVS.append((x_coordinate[i], y_coordinate[i]))
            sheet = book.sheet_by_name('lamp_pos_map'+str(self.map_number))
            pos_tmp = [x for x in sheet.col_values(1)]
            for i in range(1, len(pos_tmp)):
                TRAFFIC_LAMP_POS.append(int(pos_tmp[i]))
            sheet = book.sheet_by_name('lamp_coordinates_map'+str(self.map_number))
            x_coordinate = [x for x in sheet.col_values(1)]
            y_coordinate = [y for y in sheet.col_values(2)]
            direction = [direction for direction in sheet.col_values(3)]
            index = [index for index in sheet.col_values(4)]

            for i in range(1, len(x_coordinate)):
                TRAFFIC_LAMP_COORDINATES.append((x_coordinate[i], y_coordinate[i], direction[i], index[i]))

