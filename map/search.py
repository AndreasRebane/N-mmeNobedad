

global buildingCount
buildingCount = 0

class placeInfo:
    officialName = "NAMEHERE"
    xCordinate = 0
    yCordinate = 0
    nameSynonyms = {}
    subPlaces = []
    id = 0
    def __init__(self, __xCordinate: int, __yCordinate: int, __nameSynonys: list, __officialName: str, __subPlaces: list) -> None:
        self.xCordinate = __xCordinate
        self.yCordinate = __yCordinate
        self.nameSynonyms = __nameSynonys #list
        self.officialName = __officialName
        self.subPlaces = __subPlaces
        global buildingCount
        self.id = buildingCount
        buildingCount += 1
        pass

oppehoone1 = placeInfo(0, 0, ["study building 1", "uo1"], "õppehoone 1", ["aula", "main hall", "infolaud", "garderoob", "colakroom", "söökla", "cafeteria", "hoiukarp", "lockers", "seb pangaautomaat", "atm(seb)", "telefoniautomaadid", "pay phones", "turundus- ja kommunikatsiooni osakond", "marketing and communications office"])
oppehoone2 = placeInfo(0, 0, ["study building 2","uo2"], "õppehoone 2", ["infotehnoloogia teaduskond", "faculty of information technology"])
oppehoone3 = placeInfo(0, 0, ["study building 2", "uo3"], "õppehoone 3", ["ehitusteaduskond", "faculty of civicl engineering", "rahvusvaheliste suhete osakond (II korrus)", "international relations office (2nd floor)", "kantselei", "document management office", "koolikaubad ja õpikud", "stationery and textbooks", "kohvik-, karastusjoogi- ja suupisteautomaadid", "coffee, soft drink and snack machines"])
oppehoone4 = placeInfo(0, 0, ["study building 4", "uo3"], "õppehoone 4", ["keemia- ja materiaalitehnoloogia teaduskond", "faculty of chemical and material technology", "õppeosakond", "office of academic affairs", "vastuvõtu- ja nõustamis talitus", "admission and counceling office", "paljundusteenus", "copying", "kohvik", "ttü geoloogia instituudi kivimikollektsioonide hoone", "building of geological collections of tut institute of geology"])
oppehoone5 = placeInfo(0, 0, ["study building 5", "uo5"], "õppehoone 5", ["mehaanikateaduskond", "faculty of mechanical engineering", "baltic tours'i kontor", "baltic tours travel agent", "5b. finants- ja haldusstruktuurid", "finance and administrative units"])
oppehoone6 = placeInfo(0, 0, ["study building 6", "uo6"], "õppehoone 6",["avatud ülikool", "open university", "kohvik", "cafe", "üliõpilasesindus (II korrus)", "student council (2nd floor)", "üliõpilas organisatisoon aiesec", "student organisation aiesec", "üliõpilasorganisatsioon  best-estonia", "student organization best-estonia"])
oppehoone7 = placeInfo(0, 0, ["study building 7", "uo7"], "õppehoone 7",["energeetika teaduskond", "faculty of power engineering", "rektoraat", "rectors' office", "nõukogu saal", "university council hall "])
loodusteadustemaja = placeInfo(0,0, ["building of natural scinece", "sci"], "loodusteaduste maja", ["matemaatika-loodusteaduskond", "faculty of science"])

global buildingList
buildingList = [oppehoone1, oppehoone2, oppehoone3, oppehoone4, oppehoone5]


def findClosestMatch(searchString: str):
    closestMachIDList = []
    
    for x in buildingList:
        
        # Kui antud stringis on sarnasusi official nimega salvesta official nimi listi ja uuri teisi hooneid nyyd
        if (x.officialName.lower().find(searchString.lower()) != -1):
            closestMachIDList.append(x.id)
        else:
            for subNames in x.nameSynonyms:
                if subNames.lower().find(searchString.lower()) != -1:
                    closestMachIDList.append(x.id)
    return closestMachIDList

def getBuildingInstance(id: int):
    for x in buildingList:
        if (id == x.id):
            return x
    return -1