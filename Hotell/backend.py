import time

roomCategoryList = ["None", "Single", "Double", "Twin"]

class hotelInfo:
    roomCounter = 0

class roomData:
    def __init__(self, rG, nP) -> None:
        hotelInfo.roomCounter = hotelInfo.roomCounter + 1
        self.roomNumber = hotelInfo.roomCounter
        self.roomCategory = roomCategoryList[rG]
        self.dayPrice = nP
        pass
    roomNumber = 0
    roomCategory = roomCategoryList[0]
    roomCost = 0
    bookData = {0: {"startDate": "01.01.2000", "endDate": "01.01.2000", "customer": "customerName", "totalCost": 0}}


defaultRoom = roomData(1, 90)
allRooms = {defaultRoom}


def createRoom(category, price):
    allRooms.add(roomData(category, price))


def getRoomInstance(roomNumber):
        for room in allRooms:
            if (room.roomNumber == roomNumber):
                return room
        return -1

def bookRoom(roomNumber, customerName, bookingBeginDate, bookingEndDate):
    roomInstance = getRoomInstance(roomNumber)
    if (roomInstance == -1): 
        print("Room doesn't exist")
        return 0
    
    # Is the date available?
    for x in roomInstance.bookData:
        start = roomInstance.bookData[x]["startDate"]
        end = roomInstance.bookData[x]["endDate"]

        
        print(end)

    
    


