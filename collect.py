import requests
from datetime import datetime, timezone 
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


def count_bikes(station,bike_type):
    for vehicle in station["vehicle_types_available"]:
        if vehicle["vehicle_type_id"] == bike_type :
            return vehicle["count"] 
    return 0 

first = stations_active[0]
print(count_bikes(first, "mechanical"))
print(count_bikes(first, "electrical"))    


def to_utc(secondes):
    return datetime.fromtimestamp(secondes, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

print(to_utc(1793207798)) 


def station_to_row(station, timestamp_utc):
    return {
        "timestamp_utc": timestamp_utc,
        "station_id": station["station_id"],
        "mechanical_bikes_available": count_bikes(station, "mechanical"),
        "electric_bikes_available": count_bikes(station, "electrical"),
        "bikes_out_of_service": station["num_bikes_disabled"],
        "docks_available": station["num_docks_available"],
        "docks_out_of_service": station["num_docks_disabled"],
        "can_rent": int(station["is_renting"]),
        "can_return": int(station["is_returning"]),
        "last_reported_utc": to_utc(station["last_reported"]),
    }

timestamp_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
print(station_to_row(stations_active[0], timestamp_utc))


