from time import sleep
from locationSearch import *
from pathfinding import *
from random import *


#locations = searchForLocation()

#draw_path(locations.xStartPos, locations.yStartPos, locations.xEndPos, locations.yEndPos)
rand1 = randint(0, buildingCount -1)
rand2 = randint(0, buildingCount -1)
draw_path(buildingList[rand1].xCordinate, buildingList[rand1].yCordinate, buildingList[rand2].xCordinate, buildingList[rand2].yCordinate)


while (True):
    sleep(0.1)