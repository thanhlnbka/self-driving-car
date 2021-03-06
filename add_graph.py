import math as mt
from dijkstra import DijkstraSPF, Graph
alfa = "abcdefghijklmnopqrstuvwxyzABCDEFG"
def dis_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dis_p = mt.sqrt(mt.pow((x1-x2),2)+mt.pow((y1-y2),2))
    return int(dis_p)

def create_datadict(path_toado = "./etractpoint/map_ledaihanh_map8.txt"):
    
    global alfa
    with open(path_toado, "rb") as fs:
        data = fs.readlines()
    data_dict = dict()
    for i in range(len(data)):
        m = str(data[i])
        point = m[2:-3].split(",")
        point.append(alfa[i])
        data_dict["{}".format(i+1)] = point
    return data_dict


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
    s,t,u,v,w,x,y,z,A,B,C,D,E,F = nodes = list(alfa)
    data_dict_alfa= create_datadict_alfa()
    # print(data)
    graph = Graph()
    with open(path_vitri_alfa,"rb") as f_alfa:
        vitri = f_alfa.readlines()
        for i in vitri:
            nodes = str(i)[2:-3].split(",")
            # print(nodes)
            # print(data["{}".format(nodes[0])])
            for n in range(1, len(nodes)):
                distance = dis_points(data_dict_alfa["{}".format(nodes[0])], \
                    data_dict_alfa["{}".format(nodes[n])])
                graph.add_edge(nodes[0],nodes[n],distance)

    return graph


def convert_alfa():
    with open("etractpoint/map_vitri_map8.txt") as fs:
        vitri = fs.readlines()
        # print(node)
        data = create_datadict()
        for i in range(len(vitri)):
            node = vitri[i][:-1].split(",")
            print(node)
            str_ = ""
            for j in range(len(node)):
                str_ += data["{}".format(node[j])][2] + ","
            with open("etractpoint/map_vitri_alfa_map8.txt","a") as f:
                f.writelines(str_[:-1] + "\n")

def get_near_point(data_alfa,point):
    m = 10000
    for k, v in data_alfa.items():
        a = dis_points(v, point)
        if m >= a:
            m = a
            point_near = k
    return point_near

if __name__ == "__main__":
    convert_alfa()
    # graph = add_graph()
    # point_click = [(895, 582), (225, 25)]
    # point_one = point_click[0]
    # point_two = point_click[1]
    # data_alfa = create_datadict_alfa()
    # point_start = get_near_point(data_alfa, point_one)
    # point_end = get_near_point(data_alfa, point_two)
    # dijkstra = DijkstraSPF(graph,point_start)
    # print(dijkstra.get_path(point_end))
    # lotrinh = dijkstra.get_path(point_end)
    # MAP_NAVS = [tuple(data_alfa[i]) for i in lotrinh ]
    # print(MAP_NAVS)
    # pass
