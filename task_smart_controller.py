"""
Lab 4 - Tiny smart controller project.
Doc DHT20, ap dung logic local, va phan hoi bang display.
"""

from yolobit import *
from lib.aiot.aiot_dht20 import DHT20

dht = None
mode = "UNKNOWN"


def task_init():
    global dht, mode
    mode = "UNKNOWN"
    try:
        dht = DHT20()
        print("[LAB4] Smart controller ready")
    except Exception as err:
        dht = None
        print("[LAB4] DHT20 error:", err)


def task_run():
    global mode
    if not dht:
        return

    try:
        temp = dht.dht20_temperature()
        hum = dht.dht20_humidity()

        if temp >= 30 and hum >= 70:
            mode = "HOT_HUMID"
            display.show(Image.ANGRY)
        elif temp <= 20 and hum <= 50:
            mode = "COLD_DRY"
            display.show(Image.SAD)
        else:
            mode = "NORMAL"
            display.show(Image.HAPPY)

        print("[LAB4] T={:.1f}C H={:.1f}% MODE={}".format(temp, hum, mode))
    except Exception as err:
        print("[LAB4] read error:", err)
