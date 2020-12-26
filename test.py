MAP_NAVS = [(23, 627), (247, 626), (558, 626), (727, 624), (925, 625), (0, 0)]
print(MAP_NAVS)
def gener_MAP_NAVS(MAP_NAVS, number_leng =  4):
    a = 1
    dict_insert = dict()
    for p in range(len(MAP_NAVS)-1):
        dis_x = MAP_NAVS[p][0]-MAP_NAVS[p+1][0]
        dis_y = MAP_NAVS[p][1]-MAP_NAVS[p+1][1]
        arr_insert = []
        if abs(dis_x) <= 5:
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
                arr_insert = [(MAP_NAVS[p][0]+k_x*i, max_y) for i in range(1,number_leng)]
            dict_insert[a] = arr_insert
            a = a + number_leng

        
    for k,v in dict_insert.items():
        MAP_NAVS[k:k] = v
    return MAP_NAVS
map_navs = gener_MAP_NAVS(MAP_NAVS, number_leng=2)
print(map_navs)
# import cv2
# path = "/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/map8.png"
# image = cv2.imread(path)
# image = cv2.resize(image, (940,640))
# cv2.imwrite("/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/map8_940_640.png",image)
#