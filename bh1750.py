#!/usr/bin/python
# --------------------------------------
#  Read data from a digital light sensor.
#
#  Official datasheet available from :
#  https://www.mouser.com/ds/2/348/bh1750fvi-e-186247.pdf
#
# Author : Raúl Caro Pastorino
# Date   : 01/08/2019
#
# --------------------------------------
import smbus
import time

class BH1750:
    DEVICE = 0x23      # Default device I2C address
    POWER_DOWN = 0x00  # No active state
    POWER_ON = 0x01    # Power on
    RESET = 0x07       # Reset data register value
    ONE_TIME_HIGH_RES_MODE = 0x20
    bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

    def __init__(self, device=0x23):
        self.DEVICE = device


