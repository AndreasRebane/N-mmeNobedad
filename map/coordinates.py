class totalBuildings:
    count = 0

class placeInfo:
    def __init__(self, __xCordinate, __yCordinate, __nameSynonys, __officialName) -> None:
        self.xCordinate = __xCordinate
        self.yCordinate = __yCordinate
        self.nameSynonyms = __nameSynonys #list
        self.officialName = __officialName
        pass
    id = totalBuildings.count
    totalBuildings.count = totalBuildings.count + 1
    officialName = "NAMEHERE"
    xCordinate = 0
    yCordinate = 0
    nameSynonyms = {"NONE"}