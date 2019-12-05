#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import digitalio

print("hello blinky!")

# led = digitalio.DigitalInOut(board.LED_RED)

# led = digitalio.DigitalInOut(board.LED_GREEN)
# led = digitalio.DigitalInOut(board.BATT_LED_1)
# led = digitalio.DigitalInOut(board.BATT_LED_2)
# led = digitalio.DigitalInOut(board.BATT_LED_3)
# led = digitalio.DigitalInOut(board.BATT_LED_4)

led = digitalio.DigitalInOut(board.P9_16)

led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)


# P8_13
# P8_19
#
# P9_14
# P9_16
