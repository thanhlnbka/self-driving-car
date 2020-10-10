import pygame
import xlrd

from graphic.loader import load_image

# Map filenames.
MAP_NAVS = []

FINISH_INDEX = 0

TRAFFIC_LAMP_POS = []
TRAFFIC_LAMP_COORDINATES = []


class Map(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, map_number):
        pygame.sprite.Sprite.__init__(self)
        # print(FINISH_INDEX)
        # print(MAP_NAVS)
        # print(TRAFFIC_LAMP_POS)
        # print(TRAFFIC_LAMP_COORDINATES)
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
        with xlrd.open_workbook('/home/luuthanh/Desktop/fuzzy-logic-project/media/abc.xlsx') as book:
            # sheet = book.sheet_by_index(self.map_number - 1)
            sheet = book.sheet_by_name('Map0'+str(self.map_number))
            print(sheet.name)
            x_coordinate = [x for x in sheet.col_values(1)]
            y_coordinate = [y for y in sheet.col_values(2)]
            print(x_coordinate)
            print(y_coordinate)
            for i in range(1, len(x_coordinate)):
                MAP_NAVS.append((x_coordinate[i], y_coordinate[i]))
            print(book.sheet_names())
            sheet = book.sheet_by_name('lamp_pos_map'+str(self.map_number))
            # sheet = book.sheet_by_index(self.map_number + 5)
            pos_tmp = [x for x in sheet.col_values(1)]
            print(pos_tmp)
            print(sheet.name)
            # print(pos_tmp)
            for i in range(1, len(pos_tmp)):
                # print(pos_tmp[i])
                TRAFFIC_LAMP_POS.append(int(pos_tmp[i]))
            # print("TRAFFIC LAMP POS: ", TRAFFIC_LAMP_POS)
            sheet = book.sheet_by_name('lamp_coordinates_map'+str(self.map_number))
            # sheet = book.sheet_by_index(self.map_number + 11)
            print(sheet.name)
            x_coordinate = [x for x in sheet.col_values(1)]
            y_coordinate = [y for y in sheet.col_values(2)]
            direction = [direction for direction in sheet.col_values(3)]
            index = [index for index in sheet.col_values(4)]

            for i in range(1, len(x_coordinate)):
                TRAFFIC_LAMP_COORDINATES.append((x_coordinate[i], y_coordinate[i], direction[i], index[i]))

