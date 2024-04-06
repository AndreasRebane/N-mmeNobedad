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