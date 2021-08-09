import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import serial
from serial import Serial

# The code below creates a live plot that plots in front of us.
# Adjust as needed: x and y axes (voltage up to 600, ec)
                  # pressure data
                  # currently, voltage = dummy data from arduino
                  # with the timeInc/time additions, this graph plots the dummy
                         # arduino data versus time (x, increments of 1)
                         # cc=str(ser.readline()) and cc[2:][:-5] display live data
                              # from arduino

timeInc = 0
voltage = []
time = []
pressure = []

#               ymax should be 600 volts for voltage
plt.axis([0, 100, 0, 600])

                    #change address as needed (check Arduino IDE->tools for this)
ser = serial.Serial("/dev/cu.usbmodem141301", 9600)
for i in range(0, 101)
    cc=str(ser.readline())
    timeInc += 1
    time += [timeInc]
    voltage += [cc[2:][:-5]]
    pressure += [np.random.random()] #pressure just has random np values for the purpose of testing
    plt.plot(time, voltage, linewidth = 1,
         marker='o', markerfacecolor='black', markersize=2)
    plt.pause(0.005)

plt.show()
