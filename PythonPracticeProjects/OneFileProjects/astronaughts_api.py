import requests

response = requests.get("http://api.open-notify.org/astros.json") # Requests the API data and assigns it to response
data = response.json() # Converts the JSON to python and stores it in data as a dictionairy
in_space_count = data.get("number") # Gets the value associated with the "number" key and assigns it to "in_space_count"
print(f"There are {in_space_count} astronaughts in space.") # Prints how many astronaughts there are in space
