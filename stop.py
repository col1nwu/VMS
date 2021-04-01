import os


def stop():
    file = open("./data/pid.txt", "w")

    pid1 = file.readline()
    pid2 = file.readline()
    pid3 = file.readline()

    os.system("kill " + pid1)
    os.system("kill " + pid2)
    os.system("kill " + pid3)


if __name__ == "__main__":
    stop()
