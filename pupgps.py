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

To set up the GPSD module, watch this video: https://www.youtube.com/watch?v=isVHkovZuSM
"""

dest_lat = 40.4214
dest_lon = -86.9202


def Navidata(dest_lat, dest_lon, vid):
    gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

    while True:
        report = gpsd.next()  #
        if report['class'] == 'TPV':
            lat = getattr(report, 'lat', 0.0)
            lon = getattr(report, 'lon', 0.0)
            # Vector Calculation for computing Azimutj
            dest_vec = np.array(
                [np.cos(dest_lat) * np.cos(dest_lon), np.cos(dest_lat) * np.sin(dest_lon), np.sin(dest_lat)])
            curr_vec = np.array([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)])
            normal = np.array([0, 0, 1])
            normal_curr_n = np.cross(curr_vec, normal)
            normal_curr_dest = np.cross(curr_vec, dest_vec)
            angle = np.arccos(np.dot(norm(normal_curr_n), norm(normal_curr_dest))) * 180 / math.pi
            manual_azimuth = math.atan2(np.sin(dest_lon - lon) * np.cos(dest_lat),
                                        np.cos(lat) * np.sin(dest_lat) - np.sin(lat) * np.cos(dest_lat) * np.cos(
                                            dest_lon - lon)) * 180 / math.pi
            # Get Azimuth from geographiclibary
            brng = Geodesic.WGS84.Inverse(lat, lon, dest_lat, dest_lon)['azi1']
            data = str(lat) + " " + str(lon) + " " + vid

            # Print output; format: date | time | latitude | longitude
            os.system("echo " + str(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + data + " >> ./data/gps_data.txt")

            # Set a time interval: 2 sec
            time.sleep(2)


if __name__ == "__main__":
    Navidata(dest_lat, dest_lon, sys.argv[1])
