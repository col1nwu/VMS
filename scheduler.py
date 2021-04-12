import sys

"""
Job Scheduler
PUP-2, 2021 ABE Capstone

This program connects to the Google Maps and retrieve route info from there.
IMPORTANT: no space should exist in the coordinate files!

This program is modified based on https://github.com/mkudija/blog/tree/master/content/downloads/code/google-maps-api
"""


def get_route_info(apiKey, origin, destination):
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin, destination, apiKey))

    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        drive_time = resp_json_payload['rows'][0]['elements'][0]['duration']['value'] / 60
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        drive_time = 0

    return drive_time


if __name__ == '__main__':
    # Get API Key for the Google Maps service
    fname = "APIKey.txt"
    file = open(fname, 'r')
    apiKey = file.read()
    file.close()

    file = open("./data/gps_data.txt", "r")
    start = file.readlines()
    if len(start) == 0:
        print("No location information yet...")
        sys.exit(1)
    origin = start[len(start) - 1]

    file = open("dest.txt", "r")
    dests = file.readlines()
    file.close()

    min_time = float("inf")
    opt_dest = -1
    index = 0
    for dest in dests:
        drive_time = get_route_info(apiKey, origin, dest)
        if drive_time < min_time:
            min_time = drive_time
            opt_dest = index
        index += 1

    print('Origin:      {}\nDestination: {}\nDrive Time:  {} min'.format(origin, opt_dest, round(min_time, 1)))
