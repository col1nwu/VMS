import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


def stop():
    # Open pid files and read pid
    file = open("./data/pid.txt", "r")

    pid1 = file.readline().strip()
    pid2 = file.readline().strip()
    pid3 = file.readline().strip()

    file.close()

    # For testing purpose
    print(pid1)
    print(pid2)
    print(pid3)

    # Kill three Python processes
    os.system("kill " + pid1)
    os.system("kill " + pid2)
    os.system("kill " + pid3)

    # Turn down the LED's in case they are on when the system is shut down
    GPIO.output(23, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)


if __name__ == "__main__":
    stop()
