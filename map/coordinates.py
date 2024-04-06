class totalBuildings:
    count = 0

class placeInfo:
    officialName = "NAMEHERE"
    xCordinate = 0
    yCordinate = 0
    nameSynonyms = {}
    subPlaces = []
    
    def __init__(self, __xCordinate: int, __yCordinate: int, __nameSynonys: list, __officialName: str, __subPlaces: list) -> None:
        self.xCordinate = __xCordinate
        self.yCordinate = __yCordinate
        self.nameSynonyms = __nameSynonys #list
        self.officialName = __officialName
        self.subPlaces = __subPlaces
        pass
    id = totalBuildings.count
    totalBuildings.count = totalBuildings.count + 1


oppehoone1 = placeInfo(0, 0, ["study building 1"], "õppehoone 1", ["aula", "main hall", "infolaud", "garderoob", "colakroom", "söökla", "cafeteria", "hoiukarp", "lockers", "seb pangaautomaat", "atm(seb)", "telefoniautomaadid", "pay phones", "turundus- ja kommunikatsiooni osakond", "marketing and communications office"])

buildingsList = {oppehoone1}

