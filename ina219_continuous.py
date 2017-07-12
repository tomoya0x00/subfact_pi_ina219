#!/usr/bin/python

from Subfact_ina219 import INA219
import time

ina = INA219()

print "Shunt   : %.3f mV" % ina.getShuntVoltage_mV()
print "Bus     : %.3f V" % ina.getBusVoltage_V()
print "Current : %.3f mA" % ina.getCurrent_mA()

print "Shun[mV],Bus[V],Current[mA],Power[mW]"

while True:
    print "%.3f,%.3f,%.3f,%.3f" % ( ina.getShuntVoltage_mV(), ina.getBusVoltage_V(), ina.getCurrent_mA(), ina.getPower_mW() )
    time.sleep(0.001)
