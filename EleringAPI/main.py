import requests
import json
import time
#with open('file.txt', 'w') as file:


print(time.localtime())

year, month, day, hour, minute, second, g, h, i = time.localtime()

targetURL = f"https://dashboard.elering.ee/api/nps/price?start={year}-0{month}-0{day}T01%3A00%3A00.999Z&end={year}-0{month}-0{day+1}T23%3A59%3A59.999Z"


def performAPICall(url):
    results = requests.get(url)
    if (results.status_code != 200):
        return 0
    return results.json()

def filterAPICall(jsonResults):
    data = jsonResults["data"]["ee"][0]
    
    for x in jsonResults["data"]["ee"]:
        print(x["price"])
    
    


data = performAPICall(targetURL)
filterAPICall(data)