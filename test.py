#!/usr/bin/python
# --------------------------------------
#  Test sensor.
#
#  Official datasheet available from :
#  https://www.mouser.com/ds/2/348/bh1750fvi-e-186247.pdf
#
# Author : Raúl Caro Pastorino
# Date   : 01/08/2019
#
# --------------------------------------
from time import sleep
from bh1750 import BH1750

sensor = BH1750()

while True:
    print(sensor.read_light_format_string())
    sleep(1)
