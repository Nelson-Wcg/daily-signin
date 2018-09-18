import os
import time


def click(x, y, sleep=2):
    swipe(x, y, x, y, 10, sleep)
    # os.system("adb shell input swipe " + str(x) + " " + str(y) + " " + str(x) + " " + str(y) + " 10")


def open_app(package, main_class):
    print("adb shell am start " + package + "/" + main_class)
    os.system("adb shell am start " + package + "/" + main_class)
    time.sleep(10)


def close(package):
    os.system("adb shell am force-stop " + package)
    time.sleep(1)


def swipe(x, y, x1, y1, swipe_time, sleep=2):
    print("adb shell input swipe " + str(x) + " " + str(y) + " " + str(x1) + " " + str(y1) + " " + str(swipe_time))
    os.system("adb shell input swipe " + str(x) + " " + str(y) + " " + str(x1) + " " + str(y1) + " " + str(swipe_time))
    time.sleep(sleep)


def back():
    os.system("adb shell input keyevent 4")
    time.sleep(1)
