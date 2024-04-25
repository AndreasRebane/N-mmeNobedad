from time import sleep
from locationSearch import *
from pathfinding import *


locations = searchForLocation()
draw_path(locations.xStartPos, locations.yStartPos, locations.xEndPos, locations.yEndPos)