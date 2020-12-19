with open("./etractpoint/map_ledaihanh.txt", "rb") as fs:
    data = fs.readlines()
data_dict = dict()
alfa = "abcdefghijklmnopqrstuvwxyzABCDEF"
for i in range(len(data)):
    m = str(data[i])
    point = m[2:-3].split(",")
    point.append(i+1)
    # print(point)
    data_dict["{}".format(alfa[i])] = point
# print(data_dict)
print(data_dict)
# print(len(data_dict))
    
  