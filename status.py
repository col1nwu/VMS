
"""
Status Checker, Vehicle Monitoring System
Colin Wu, wu1418@purdue.edu
@version: 3/2/21

Check status for the vehicle. Raise flags if necessary.
"""

eng_speed_limit = 2000


def check_eng_speed(filename):
    # Retrieve engine speed data
    f = open(filename)
    data = f.readline().split()

    max_speed = max(data)
    if int(max_speed) > eng_speed_limit:
        return True


def change_eng_speed_limit(num):
    global eng_speed_limit
    eng_speed_limit = num


if __name__ == "__main__":
    # inp = input("Set the engine speed limit: ")
    # change_eng_speed_limit(int(inp))

    if check_eng_speed("eng_speed.txt"):
        print("Engine speed alert!")
