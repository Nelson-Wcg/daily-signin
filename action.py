import os
import time


def click(x, y):
    os.system("adb shell input text sdfsdf" + str(x) + str(y))
    time.sleep(2)


def open_app(package, main_class):
    os.system("adb shell am start " + package + "/" + main_class)
    time.sleep(4)


def class_app(main_class):
    os.system("adb shell am force-stop " + main_class)

