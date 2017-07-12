#!/usr/bin/python

from Subfact_ina219 import INA219
import time

ina = INA219()

print "Time,Shunt[mV],Bus[V],Current[mA]"

while True:
    print "%.3f,%.3f,%.3f,%.3f" % ( time.time(), ina.getShuntVoltage_mV(), ina.getBusVoltage_V(), ina.getCurrent_mA())
    time.sleep(0.001)
