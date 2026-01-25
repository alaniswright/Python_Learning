def get_station_data(filename: str):
    dict_of_stations = {}
    with open(filename) as my_file:
        next(my_file)
        for line in my_file:
            l = line.split(";")
            dict_of_stations[l[3]] = (float(l[0]), float(l[1]))
    return dict_of_stations

def distance(stations: dict, station1: str, station2: str):
    import math

    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    longest_distance = 0
    s1 = ""
    s2 = ""
    for station_a in stations:
        for station_b in stations:
            ld =  distance(stations, station_a, station_b) 
            if ld > longest_distance:
                longest_distance = ld
                s1 = station_a
                s2 = station_b
    return(s1, s2, longest_distance)



if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)