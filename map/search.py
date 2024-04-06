

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

oppehoone1 = placeInfo(525, 533, ["study building 1", "uo1"], "õppehoone 1", ["aula", "main hall", "infolaud", "garderoob", "colakroom", "söökla", "cafeteria", "hoiukarp", "lockers", "seb pangaautomaat", "atm(seb)", "telefoniautomaadid", "pay phones", "turundus- ja kommunikatsiooni osakond", "marketing and communications office"])
oppehoone2 = placeInfo(468, 499, ["study building 2","uo2"], "õppehoone 2", ["infotehnoloogia teaduskond", "faculty of information technology"])
oppehoone3 = placeInfo(478, 477, ["study building 2", "uo3"], "õppehoone 3", ["ehitusteaduskond", "faculty of civicl engineering", "rahvusvaheliste suhete osakond (II korrus)", "international relations office (2nd floor)", "kantselei", "document management office", "koolikaubad ja õpikud", "stationery and textbooks", "kohvik-, karastusjoogi- ja suupisteautomaadid", "coffee, soft drink and snack machines"])
oppehoone4 = placeInfo(492, 454, ["study building 4", "uo3"], "õppehoone 4", ["keemia- ja materiaalitehnoloogia teaduskond", "faculty of chemical and material technology", "õppeosakond", "office of academic affairs", "vastuvõtu- ja nõustamis talitus", "admission and counceling office", "paljundusteenus", "copying", "kohvik", "ttü geoloogia instituudi kivimikollektsioonide hoone", "building of geological collections of tut institute of geology"])
oppehoone5 = placeInfo(506, 429, ["study building 5", "uo5"], "õppehoone 5", ["mehaanikateaduskond", "faculty of mechanical engineering", "baltic tours'i kontor", "baltic tours travel agent", "5b. finants- ja haldusstruktuurid", "finance and administrative units"])
oppehoone6 = placeInfo(513, 401, ["study building 6", "uo6"], "õppehoone 6",["avatud ülikool", "open university", "kohvik", "cafe", "üliõpilasesindus (II korrus)", "student council (2nd floor)", "üliõpilas organisatisoon aiesec", "student organisation aiesec", "üliõpilasorganisatsioon  best-estonia", "student organization best-estonia"])
oppehoone7 = placeInfo(556, 553, ["study building 7", "uo7"], "õppehoone 7",["energeetika teaduskond", "faculty of power engineering", "rektoraat", "rectors' office", "nõukogu saal", "university council hall "])
loodusteadustemaja = placeInfo(805, 374, ["building of natural scinece", "sci"], "loodusteaduste maja", ["matemaatika-loodusteaduskond", "faculty of science"])
uliopilaselamu1 = placeInfo(613, 485, ["student hostel 1", "do1"], "üliõpilaselamu 1", [""])
uliopilaselamu2 = placeInfo(635, 433, ["student hostel 2", "do2"], "üliõpilaselamu 2", [""])
uliopilaselamu3 = placeInfo(654, 394, ["student hostel 3", "do3"], "üliõpilaselamu 3", [""])
pereuhiselamu = placeInfo(650, 473, ["family hostel ", "do4"], "pereühiselamu", [""])
academichostel = placeInfo(714, 400, ["academic hostel ", "hos"], "pereühiselamu", [""])
uliopilaselamu11 = placeInfo(736, 390, ["student hostel 11", "do7"], "üliõpilaselamu 11", [""])
uliopilaselamu4d = placeInfo(715, 349, ["student hostel 4d", "do6"], "üliõpilaselamu 4d", ["ttü üliõpilasküla", "student village of tut"])
itmaja = placeInfo(703, 237, ["it building", "mek"], "it maja", ["infotehnoloogia teaduskond", "faculty of information technology", "ttü it täiendõppekeskus", "it further education center of tut", "kohvik", "cafe"])
ehitusteaduskonnalaborihoone = placeInfo(0, 0, ["laboratory builsing of civil engineering", "con"], "ehitusteaduskonna laborihoone", [""])
itkolledz = placeInfo(773, 181, ["it college", "ico"], "it kolledž", [""])
tehnoloogiapark = placeInfo(676, 343, ["technology park", "itc"], "tehnoloogiapark", [""])
kuberneetikamaja = placeInfo(880, 290, ["building of cybernetics", "cyb"], "küberneetikamaja", ["ttü küberneetika instituut", "institute of cybernetics at tut", "ttü meresüsteemida instituut", "institute of marine systems at tut"])
puidumaja = placeInfo(846, 401, ["building of woodworking", "tim"], "puidumaja", ["puidutöötlemise õppetool", "chair of woodworking"])
staadion = placeInfo(982, 298, ["stadium", "sta"], "staadion", [""])
tekstiilimaja = placeInfo(572, 291, ["textile technology building", "tex"], "tekstiilimaja", ["disaini lektoraat", "chair of design", "tekstiilitehnoloogia õppetool", "chair of textile technology"])
spordikeskus = placeInfo(217, 559, ["sports center", "so1"], "spordikeskus", [""])
oppehoone10 = placeInfo(274, 603, ["study buoilding 10", "uo7"], "õppehoone 10", ["majandusteaduskond", "tallinn school of economics and bussiness administration", "sotsiaalteaduskond", "faculty of social sciences", "ttü majandusteaduskonna koolituskeskus", "center for economic education of faculty of economics and bussiness administration at tut", "keeltekeskus", "language center", "söökla", "cafeteria", "postkontor ja meened", "post office and souvenirs", "swedbanki kontor", "swedbank branch", "lillepood", "florist"])

global buildingList
buildingList = [oppehoone1, oppehoone2, oppehoone3, oppehoone4, oppehoone5, oppehoone6, oppehoone7, loodusteadustemaja, uliopilaselamu1, uliopilaselamu2, uliopilaselamu3, pereuhiselamu, academichostel, uliopilaselamu11, uliopilaselamu4d, itmaja, ehitusteaduskonnalaborihoone, itkolledz, tehnoloogiapark, kuberneetikamaja, puidumaja, staadion, tekstiilimaja, spordikeskus, oppehoone10]


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

    
