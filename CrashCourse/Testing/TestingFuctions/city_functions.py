def CityCountry(city, country, population=""):
    if population == "":
        return city + ", " + country
    else:
        return city + ", " + country + " - population " + population