import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def stop():
    file = open("./data/pid.txt", "r")

    pid1 = file.readline().strip()
    pid2 = file.readline().strip()
    pid3 = file.readline().strip()

    print(pid1)
    print(pid2)
    print(pid3)

    os.system("kill " + pid1)
    os.system("kill " + pid2)
    os.system("kill " + pid3)

    # Shut down the LED's too
    GPIO.output(23, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)

if __name__ == "__main__":
    stop()
