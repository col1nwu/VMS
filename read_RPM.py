import datetime
import time
import pigpio  # http://abyz.co.uk/rpi/pigpio/python.html
import os
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)

"""
RPM Data Fetcher
PUP-2, 2021 ABE Capstone

This file contains functions which get RPM reading from Hall effect sensor.
The RPM LED is on the right. It is connected to GPIO 23.

This file is modified based on code in https://github.com/gingerbreadassassin/RPiFanController
"""


class reader:
    """
   A class to read speedometer pulses and calculate the RPM.
   """

    def __init__(self, pi, gpio, pulses_per_rev=1.0, weighting=0.0, min_RPM=5.0):
        """
      Instantiate with the Pi and gpio of the RPM signal
      to monitor.
      Optionally the number of pulses for a complete revolution
      may be specified.  It defaults to 1.
      Optionally a weighting may be specified.  This is a number
      between 0 and 1 and indicates how much the old reading
      affects the new reading.  It defaults to 0 which means
      the old reading has no effect.  This may be used to
      smooth the data.
      Optionally the minimum RPM may be specified.  This is a
      number between 1 and 1000.  It defaults to 5.  An RPM
      less than the minimum RPM returns 0.0.
      """
        self.pi = pi
        self.gpio = gpio
        self.pulses_per_rev = pulses_per_rev

        if min_RPM > 1000.0:
            min_RPM = 1000.0
        elif min_RPM < 1.0:
            min_RPM = 1.0

        self.min_RPM = min_RPM

        self._watchdog = 200  # Milliseconds.

        if weighting < 0.0:
            weighting = 0.0
        elif weighting > 0.99:
            weighting = 0.99

        self._new = 1.0 - weighting  # Weighting for new reading.
        self._old = weighting  # Weighting for old reading.

        self._high_tick = None
        self._period = None

        pi.set_mode(gpio, pigpio.INPUT)

        self._cb = pi.callback(gpio, pigpio.RISING_EDGE, self._cbf)
        pi.set_watchdog(gpio, self._watchdog)

    def _cbf(self, gpio, level, tick):

        if level == 1:  # Rising edge.

            if self._high_tick is not None:
                t = pigpio.tickDiff(self._high_tick, tick)

                if self._period is not None:
                    self._period = (self._old * self._period) + (self._new * t)
                else:
                    self._period = t

            self._high_tick = tick

        elif level == 2:  # Watchdog timeout.

            if self._period is not None:
                if self._period < 2000000000:
                    self._period += (self._watchdog * 1000)

    def RPM(self):
        """
      Returns the RPM.
      """
        RPM = 0.0
        if self._period is not None:
            RPM = 60000000.0 / (self._period * self.pulses_per_rev)
            if RPM < self.min_RPM:
                RPM = 0.0

        return RPM

    def cancel(self):
        """
      Cancels the reader and releases resources.
      """
        self.pi.set_watchdog(self.gpio, 0)  # cancel watchdog
        self._cb.cancel()


if __name__ == "__main__":
    import time
    import pigpio
    import read_RPM

    """
    IMPORTANT: The line below specifies the pin number.
    If the Hall effect sensor is connected to a wrong pin, it will generate random RPM readings.
    """
    RPM_GPIO = 14

    ################################
    #                              #
    # Change probing interval here #
    #                              #
    ################################
    # The program will collect data in a certain time interval
    # The current time interval is 2 sec.
    # Change the value of SAMPLE_TIME will change the probing interval.
    SAMPLE_TIME = 2.0

    pi = pigpio.pi()
    p = read_RPM.reader(pi, RPM_GPIO)
    start = time.time()

    while True:
        time.sleep(SAMPLE_TIME)

        RPM = p.RPM()
        RPM = int(RPM + 0.5)

        #############################
        #                           #
        # Change RPM threshold here #
        #                           #
        #############################
        if RPM > 50:
            # If the RPM is above the threshold, the LED will light up
            # The current threshold is 50 rpm for testing
            GPIO.output(23, GPIO.HIGH)
        else:
            GPIO.output(23, GPIO.LOW)

        os.system("echo " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + str(RPM) +
                  " " + sys.argv[1] + " >> ./data/rpm_data.txt")

    p.cancel()

    pi.stop()
