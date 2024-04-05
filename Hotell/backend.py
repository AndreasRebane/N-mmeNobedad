import time

roomCategoryList = ["None", "Single", "Double", "Twin"]

class hotelInfo:
    roomCounter = 0

class roomData:
    roomNumber = 0
    roomCategory = roomCategoryList[0]
    roomCost = 0
    bookData = {0: {"startDate": 1, "endDate": 2, "customer": "customerName", "totalCost": 0}}
    def __init__(self, rG, nP) -> None:
        if (self.bookData.keys[0]["startDate"] == 1):
            self.bookData.clear()
        hotelInfo.roomCounter = hotelInfo.roomCounter + 1
        self.roomNumber = hotelInfo.roomCounter
        self.roomCategory = roomCategoryList[rG]
        self.roomCost = nP
        pass


defaultRoom = roomData(1, 90)
allRooms = {defaultRoom}


def createRoom(category, price):
    allRooms.add(roomData(category, price))


def getRoomInstance(roomNumber):
        for room in allRooms:
            if (room.roomNumber == roomNumber):
                return room
        return -1

def bookRoom(roomNumber, customerName, bookingBeginDate = 1, bookingEndDate = 2):
    roomInstance = getRoomInstance(roomNumber)
    if (roomInstance == -1): 
        print("Room doesn't exist")
        return 0
    
    # Is the date available?
    for x in roomInstance.bookData:
        start = roomInstance.bookData[x]["startDate"]
        end = roomInstance.bookData[x]["endDate"]

        if (bookingBeginDate > start and bookingBeginDate < end):
            print("Date is already booked")
            return 0
    
        roomInstance.bookData = {roomInstance.bookData.__len__()+1: {"startDate": bookingBeginDate, "endDate": bookingEndDate, "customer": customerName, "totalCost": (bookingEndDate-bookingBeginDate)*roomInstance.roomCost}}

def listAllBookings():
    for x in allRooms:
        for y in x.bookData:
            print(x.bookData[y]["totalCost"])

    
    


