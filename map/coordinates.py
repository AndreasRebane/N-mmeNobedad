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


<<<<<<< HEAD
oppehoone1 = placeInfo(0, 0, ["study building 1"], "õppehoone 1", ["aula", "main hall", "infolaud", "garderoob", "colakroom", "söökla", "cafeteria", "hoiukarp", "lockers", "seb pangaautomaat", "atm(seb)", "telefoniautomaadid", "pay phones", "turundus- ja kommunikatsiooni osakond", "marketing and communications office"])

buildingsList = {oppehoone1}
=======
def main():
    global buildingList
    oppehoone1 = placeInfo(0, 0, ["study building 1", "uo1"], "õppehoone 1", ["aula", "main hall", "infolaud", "garderoob", "colakroom", "söökla", "cafeteria", "hoiukarp", "lockers", "seb pangaautomaat", "atm(seb)", "telefoniautomaadid", "pay phones", "turundus- ja kommunikatsiooni osakond", "marketing and communications office"])
    oppehoone2 = placeInfo(0, 0, ["study building 2","uo2"], "õppehoone 2", ["infotehnoloogia teaduskond", "faculty of information technology"])
    oppehoone3 = placeInfo(0, 0, ["study building 2", "uo3"], "õppehoone 3", ["ehitusteaduskond", "faculty of civicl engineering", "rahvusvaheliste suhete osakond (II korrus)", "international relations office (2nd floor)", "kantselei", "document management office", "koolikaubad ja õpikud", "stationery and textbooks", "kohvik-, karastusjoogi- ja suupisteautomaadid", "coffee, soft drink and snack machines"])
    oppehoone4 = placeInfo(0,0, ["study building 4", "uo3"], "õppehoone 4", ["keemia- ja materiaalitehnoloogia teaduskond", "faculty of chemical and material technology", "õppeosakond", "office of academic affairs", "vastuvõtu- ja nõustamis talitus", "admission and counceling office", "paljundusteenus", "copying", "kohvik", "ttü geoloogia instituudi kivimikollektsioonide hoone", "building of geological collections of tut institute of geology"])
    oppehoone5 = placeInfo(0, 0, ["study building 5", "uo5"], "õppehoone 5", ["mehaanikateaduskond", "faculty of mechanical engineering", "baltic tours'i kontor", "baltic tours travel agent", "5b. finants- ja haldusstruktuurid", "finance and administrative units"])

    buildingList = [oppehoone1, oppehoone2, oppehoone3, oppehoone4, oppehoone5]
>>>>>>> cf7da4065fd611e3be66340baa7b25e4be227d66

