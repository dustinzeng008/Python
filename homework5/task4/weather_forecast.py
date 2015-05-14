import urllib.request
from urllib.error import URLError
import json
from pprint import pprint
from time import *


def secs2str(secs):
    return strftime("%Y.%m.%d %H:%M", localtime(secs))

name = input("Hi, What's your name? ")
print("Hello, " + name + "! Welcome to the search engine!")
print("Please enter address to get the weather forcast!")
searchMore = "yes"  # check if search more

while(searchMore == "yes"):
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    queryAddress = input("query: ")
    url += queryAddress
    try:
        page = urllib.request.urlopen(url)
        content = page.read()
        content_string = content.decode("utf-8")
        json_data = json.loads(content_string)
        if (json_data["cod"] == 200):
            tempeture = float(json_data["main"]["temp"]) - 273.15
            getTime = secs2str(json_data["dt"])
            wind = "Calm {0} m/s North-northwest ({1})".\
                format(json_data["wind"]["speed"], json_data["wind"]["deg"])
            cloudiness = "Cloudiness: " + json_data["weather"][0]["description"]
            pressure = "Pressure: {0} hpa".format(json_data["main"]["pressure"])
            humidity = "Humidity: {0}%".format(json_data["main"]["humidity"])
            sunrise = "Sunrise: {0}".format(secs2str(json_data["sys"]["sunrise"]).split()[1])
            sunset = "Sunset: {0}".format(secs2str(json_data["sys"]["sunset"]).split()[1])
            geo_coords = "Geo coords [ {0}, {1} ]".\
                format(json_data["coord"]["lon"], json_data["coord"]["lat"])
            print("－－－－－－－－－－－－" + queryAddress + "－－－－－－－－－－－－")
            print("get at: %s " % getTime)
            print("Current Tempeture: %.1f Celsius" % tempeture)
            print(wind)
            print(cloudiness)
            print(pressure)
            print(humidity)
            print(sunrise)
            print(sunset)
            print(geo_coords)
            print("－－－－－－－－－－－－－－－－－－-－－－－－－－－－－－")
            # pprint(json_data)
        else:
            print("Error: Not found city")

        searchMore = input("\nDo you want to search more (yes or no)? ")
        while(searchMore != "yes" and searchMore != "no"):
            searchMore = input("\nDo you want to search more (yes or no)? ")
    except URLError as e:
        print("error")

print("Bye-bye")
