import os


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


if __name__ == "__main__":
    stop()
