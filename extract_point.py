import cv2
import numpy as np 
import os 
os.environ["DISPLAY"] = ":0"
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        # print(x,y)
        with open("etractpoint/map_ledaihanh_map8.txt","a") as fs:
            fs.write("{},{}".format(x,y))
            fs.write("\n")
        mouseX,mouseY = x,y

path = "/home/luuthanh/Desktop/BTL-XLTTM/self-driving-car/media/map8.png"
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
# img = 
img = cv2.imread(path)
img = cv2.resize(img, (940,640))
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(mouseX,mouseY)
    