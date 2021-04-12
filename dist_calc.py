
"""
Distance Calculator
PUP-2, 2021 ABE Capstone

This program connects to the Google Maps and retrieve route info from there.

This program is modified based on https://github.com/mkudija/blog/tree/master/content/downloads/code/google-maps-api
"""


def get_drive_time(apiKey, origin, destination):
    """
    Returns the driving time between using the Google Maps Distance Matrix API. 
    API: https://developers.google.com/maps/documentation/distance-matrix/start


    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    origin                  [str]
    destination             [str]

    # RETURN ------------------------------------------------------------------
    drive_tim               [float] (minutes)
    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin, destination, apiKey)
           )
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        drive_time = resp_json_payload['rows'][0]['elements'][0]['duration']['value'] / 60
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        drive_time = 0
    return drive_time


if __name__ == '__main__':
    # get key
    fname = "APIKey.txt"
    file = open(fname, 'r')
    apiKey = file.read()

    # get coordinates 
    origin = "40.473105,-86.953000"
    destination = "40.416180,-86.929663"
    drive_time = get_drive_time(apiKey, origin, destination)
    print('Origin:      {}\nDestination: {}\nDrive Time:  {} hr'.format(origin, destination, drive_time / 60))
