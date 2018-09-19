import time
import datetime
import action


def test():
    now = datetime.datetime.now().strftime("%H-%M-%S")
    time_dir = {"10-00-00", "14-00-00", "18-00-00", "20-00-00", "22-00-00"}
    while True:
        print(now)
        if time_dir.__contains__(now):
            action.click(900, 1320, 0)
        now = datetime.datetime.now().strftime("%H-%M-%S")


test()
