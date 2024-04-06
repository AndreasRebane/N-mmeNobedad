from search import *

class locationParameters:
    xStartPos = 0
    yStartPos = 0
    targetBuildingID = 0

def searchForLocation():
    inputLocation = str(input("Enter Location:"))
    result: list = findClosestMatch(inputLocation)

    if (len(result) != 0):
        print("\n")
        print("Kirjuta sobiva hoone number ID: ")
        print("ID: Hoone nimi")
        for x in result:
            print(str(x) + " : " + str(buildingList[x].officialName))
        
        print("\n" * 2)
        inputID = int(input("ID:"))
        

    else:
        print("\n" * 15)
        print("Couldn't find any location with your input data. Input data: " + str(inputLocation))
        return

searchForLocation()