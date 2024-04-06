from coordinates import *

closestMachIDList = {"meow"}

def findClosestMatch(searchString: str):
    closestMachIDList.clear()
    
    for x in buildingsList:
        
        # Kui antud stringis on sarnasusi official nimega salvesta official nimi listi ja uuri teisi hooneid nyyd
        if (x.officialName.lower().find(searchString.lower()) != -1):
            closestMachIDList.add(x.id)
            return
        else:
            for subNames in x.nameSynonyms:
                if (str(subNames).lower().find(searchString.lower())):
                    closestMachIDList.add(x.id)
                    return
    
    return closestMachIDList

    
