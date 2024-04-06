from search import *
from time import sleep

#global userInputData KASUTATE ET SAADA START AND END LOCATIONI

class locationParameters:
    def __init__(self, __startX: int, __startY: int, __endX: int, __endY: int) -> None:
        self.xStartPos = __startX
        self.yStartPos = __startY
        self.xEndPos = __endX
        self.yEndPos = __endY
    pass
    xStartPos = 0
    yStartPos = 0
    xEndPos = 0
    yEndPos = 0


def searchForLocation():
    global userInputData
    inputLocation = str(input("Sisesta lõppkoht:"))
    resultID1 = peidetudLeiaHooneID(findClosestMatch(inputLocation))

    if (resultID1 == -1):
        return

    buildInstance1 = getBuildingInstance(resultID1)

    startingLocationString = str(input("Sisesta algushoone:"))
    resultID2 = peidetudLeiaHooneID(findClosestMatch(startingLocationString))

    if (resultID2 == -1):
        return
    
    buildInstance2 = getBuildingInstance(resultID2)

    userInputData = locationParameters(buildInstance2.xCordinate, buildInstance2.yCordinate, buildInstance1.xCordinate, buildInstance1.yCordinate)

    print(userInputData.xStartPos)
    print(userInputData.yStartPos)
    print(userInputData.xEndPos)
    print(userInputData.yEndPos)

    sleep(0.5)
        
def peidetudLeiaHooneID(result: list):
    if (len(result) == 0):
        print("\n" * 15)
        print("Couldn't find any location with your input data.")
        return -1
    
    print("\n")
    print("Kirjuta sobiva hoone number ID: ")
    print("ID: Hoone nimi")
    for x in result:
        print(str(x) + " : " + str(buildingList[x].officialName))
        
    print("\n" * 2)
    inputID = int(input("ID:"))
    return inputID
