import datetime
import time
import temp
import pigpio
import gps
import read_RPM
import os

"""
Driver Code
PUP-2, 2021 ABE Capstone

The main function that runs all three files and retrieves temperature, RPM, and GPS data.

Data format:
Date (y-m-d) | Time (h-m-s) | RPM | Temperature (C) | Temperature (F) | Latitude | Longitude
"""


def run():
    os.system("rm data.txt")
    RPM_GPIO = 2
    SAMPLE_TIME = 2.0

    pi = pigpio.pi()
    p = read_RPM.reader(pi, RPM_GPIO)

    # Record data from sensors each 2 second
    while True:
        time.sleep(SAMPLE_TIME)  # Loop interval

        RPM = int(p.RPM() + 0.5)
        temp_c, temp_f = temp.read_temp()
        lat, lon = gps.run()

        p.cancel()
        pi.stop()

        # Write outputs to temporary file
        os.system("echo " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + str(RPM) + " " +
                  str(temp_c) + " " + str(temp_f) + " " + str(lat) + " " + str(lon) + " >> ./data.txt")


if __name__ == "__main__":
    run()
