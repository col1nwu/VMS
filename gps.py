import os

"""
GPS Getter
PUP-2, 2021 ABE Capstone

This retrieves GPS data from GPS module and returns the latitude and longitude of current location
"""


def run():
    os.system("gpspipe -w -n 10 | grep -m 1 lon 2> /dev/null > gps.txt")

    with open("gps.txt") as f:
        raw_content = f.read()

    i = 0
    lat = 0
    lon = 0
    while True:
        if raw_content[i : i + 3] == "lat":
            lat, i = retrieve_data(raw_content, i)
        elif raw_content[i : i + 3] == "lon":
            lon, i = retrieve_data(raw_content, i)
            break

        i = i + 1

    return lat, lon


def retrieve_data(s, i):
    j = i
    while s[j] != ',':
        j = j + 1
    return float(s[i + 5: j]), j
