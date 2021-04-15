from gps import *
import math
import time
import numpy as np
from numpy.linalg import norm
from geographiclib.geodesic import Geodesic
import os
import datetime
import sys

"""
GPS Data Fetcher
PUP-2, 2021 ABE Capstone

This program receives data from GPS and GPSD modules and returns the location info, such as latitude and longitude.

Return format: date, time, latitude, longitude, altitude, speed

To set up the GPSD module, watch this video: https://www.youtube.com/watch?v=isVHkovZuSM
Reference of code: https://ozzmaker.com/using-python-with-a-gps-receiver-on-a-raspberry-pi/
"""


def Navidata(vid):
    gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

    while True:
        report = gpsd.next()  #
        if report['class'] == 'TPV':
            # Retrieve latitude, longitude, altitude, and speed
            lat = getattr(report, 'lat', 0.0)
            lon = getattr(report, 'lon', 0.0)
            alt = getattr(report, 'alt', 'nan')
            speed = getattr(report, 'speed', 'nan')

            data = str(lat) + " " + str(lon) + " " + str(alt) + " " + str(speed)
            
        if report['class'] == 'SKY':
            data += " " + str(len(gpsd.satellites)) + " " + vid
        
            # Print output; format: date | time | latitude | longitude | altitude | speed | vehicle ID
            os.system("echo " + str(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + data + " >> ./data/gps_data.txt")

            data = ""
            
            # Set a time interval: 2 sec
            time.sleep(2)


if __name__ == "__main__":
    Navidata(sys.argv[1])
