import requests

URL = "https://download.data.grandlyon.com/files/rdata/jcd_jcdecaux.jcdvelov/station_status.json"


reponse = requests.get(URL)

content = reponse.json() 

stations = content["data"]["stations"]

print(len(stations))
print(stations[0])

stations_active = [] 

for station in stations:
    if station["is_installed"]:
        stations_active.append(station)

print(len(stations_active))
