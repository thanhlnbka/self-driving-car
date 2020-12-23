import pygame
import xlrd
import math as mt
from dijkstra import DijkstraSPF, Graph
alfa = "abcdefghijklmnopqrstuvwxyzABCDEFG"
from graphic.loader import load_image
import ast
import random

MAP_NAVS = []
FINISH_INDEX = 0

TRAFFIC_LAMP_POS = []
TRAFFIC_LAMP_COORDINATES = [(132,244, 90.0, 0.0), (503,25, 90.0, 1.0)]

def dis_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dis_p = mt.sqrt(mt.pow((x1 - x2), 2) + mt.pow((y1 - y2), 2))
    return int(dis_p)

def get_near_point(data_alfa,point):
    m = 10000
    for k, v in data_alfa.items():
        a = dis_points(v, point)
        if m >= a:
            m = a
            point_near = k
    return point_near

def create_datadict_alfa(path_toado = "./etractpoint/map_ledaihanh_map8.txt"):
    global alfa
    with open(path_toado, "rb") as fs:
        data = fs.readlines()
    data_dict_alfa = dict()
    for i in range(len(data)):
        m = str(data[i])
        point = m[2:-3].split(",")
        point = [int(i) for i in point]
        data_dict_alfa["{}".format(alfa[i])] = point
    return data_dict_alfa


def add_graph(path_vitri_alfa = "./etractpoint/map_vitri_alfa_map8.txt"):
    global alfa
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,\
    s,t,u,v,w,x,y,z,A,B,C,D,E,F,G = nodes = list(alfa)
    data_dict_alfa= create_datadict_alfa()
    graph = Graph()
    with open(path_vitri_alfa,"rb") as f_alfa:
        vitri = f_alfa.readlines()
        for i in vitri:
            nodes = str(i)[2:-3].split(",")
            for n in range(1, len(nodes)):
                distance = dis_points(data_dict_alfa["{}".format(nodes[0])], \
                    data_dict_alfa["{}".format(nodes[n])])
                graph.add_edge(nodes[0],nodes[n],distance)

    return graph

def gener_MAP_NAVS(MAP_NAVS, number_leng =  4):
    a = 1
    dict_insert = dict()
    for p in range(len(MAP_NAVS)-1):
        dis_x = MAP_NAVS[p][0]-MAP_NAVS[p+1][0]
        dis_y = MAP_NAVS[p][1]-MAP_NAVS[p+1][1]
        arr_insert = []
        if abs(dis_x) <=5:
            max_x = max(MAP_NAVS[p][0],MAP_NAVS[p+1][0]) 
            k_y = abs(dis_y)//number_leng
            if dis_y >= 0:
                arr_insert = [(max_x,MAP_NAVS[p][1]-k_y*i) for i in range(1,number_leng)]
            else:
                arr_insert = [(max_x,MAP_NAVS[p][1]+k_y*i) for i in range(1,number_leng)]
            dict_insert[a] = arr_insert
            a = a + number_leng
        elif abs(dis_y) <=5:
            max_y = max(MAP_NAVS[p][1],MAP_NAVS[p+1][1]) 
            k_x = abs(dis_x)//number_leng
            if dis_x >= 0:
                arr_insert = [(MAP_NAVS[p][0]-k_x*i, max_y) for i in range(1,number_leng)]
            else:
                arr_insert = [(MAP_NAVS[p][1]+k_x*i, max_y) for i in range(1,number_leng)]
            dict_insert[a] = arr_insert
            a = a + number_leng
        
    for k,v in dict_insert.items():
        MAP_NAVS[k:k] = v
    return MAP_NAVS

class Map(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, map_number, toado_click):
        pygame.sprite.Sprite.__init__(self)
        self.map_number = map_number
        image_temp = "map"+str(map_number) + ".png"
        self.image = load_image(image_temp)
        self.rect = self.image.get_rect()
        self.x = init_x
        self.y = init_y
        self.toado_click = toado_click
        self.get_map_navs()

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x + 600, self.y - cam_y + 300

    def get_map_navs(self):
        global MAP_NAVS, TRAFFIC_LAMP_POS
        graph = add_graph()
        point_click = ast.literal_eval(self.toado_click)
        point_one = point_click[0]
        point_two = point_click[1]
        data_alfa = create_datadict_alfa()
        point_start = get_near_point(data_alfa, point_one)
        point_end = get_near_point(data_alfa, point_two)
        dijkstra = DijkstraSPF(graph, point_start)
        lotrinh = dijkstra.get_path(point_end)
        MAP_NAVS = [tuple(data_alfa[i]) for i in lotrinh]
        MAP_NAVS.append((0,0))
        MAP_NAVS = gener_MAP_NAVS(MAP_NAVS, number_leng=4)
        # TRAFFIC_LAMP_POS = []
        if (132,244) in MAP_NAVS:
            TRAFFIC_LAMP_POS.append(MAP_NAVS.index((132,244)))
        elif (503,25) in MAP_NAVS:
            TRAFFIC_LAMP_POS.append(MAP_NAVS.index((503,25)))
        TRAFFIC_LAMP_POS.sort()
        print(TRAFFIC_LAMP_POS)










    # def get_map_navs(self):
    #     with xlrd.open_workbook('/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/abc.xlsx') as book:
    #         sheet = book.sheet_by_name('Map0'+str(self.map_number))
    #         x_coordinate = [x for x in sheet.col_values(1)]
    #         y_coordinate = [y for y in sheet.col_values(2)]
            
    #         for i in range(1, len(x_coordinate)):
    #             MAP_NAVS.append((x_coordinate[i], y_coordinate[i]))
    #         print(MAP_NAVS)
    #         sheet = book.sheet_by_name('lamp_pos_map'+str(self.map_number))
    #         pos_tmp = [x for x in sheet.col_values(1)]
    #         for i in range(1, len(pos_tmp)):
    #             TRAFFIC_LAMP_POS.append(int(pos_tmp[i]))
    #         print(TRAFFIC_LAMP_POS)
    #         sheet = book.sheet_by_name('lamp_coordinates_map'+str(self.map_number))
    #         x_coordinate = [x for x in sheet.col_values(1)]
    #         y_coordinate = [y for y in sheet.col_values(2)]
    #         direction = [direction for direction in sheet.col_values(3)]
    #         index = [index for index in sheet.col_values(4)]
    
    #         for i in range(1, len(x_coordinate)):
    #             TRAFFIC_LAMP_COORDINATES.append((x_coordinate[i], y_coordinate[i], direction[i], index[i]))
    #         print(TRAFFIC_LAMP_COORDINATES)


