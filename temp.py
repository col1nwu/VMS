import os
import glob
import time
import datetime
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

"""
Temperature Data Fetcher
PUP-2, 2021 ABE Capstone

This program receives data from temperature sensor and returns the temperature in Fahrenheit and Celsius.
The temperature LED on the left. It is connected to GPIO 18.

Credit to Scott Campbell.
Source: https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/
"""

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    if len(lines) == 0:
        return 0
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        # temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


if __name__ == "__main__":
    while True:
        temp = read_temp()
        print(temp)

        #####################################
        #                                   #
        # Change temperature threshold here #
        #                                   #
        #####################################
        if temp > 30:
            # If the temperature is above the threshold, the LED will light up
            # The current threshold is 30 C for testing
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)

        os.system("echo " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + str(temp) +
                  " " + sys.argv[1] + " >> ./data/temp_data.txt")

        ################################
        #                              #
        # Change probing interval here #
        #                              #
        ################################

        # The program will collect data in a certain time interval
        # The current time interval is 2 sec.
        time.sleep(2)
