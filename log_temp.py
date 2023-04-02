#! /proyectos/anaconda3/envs/home_sensors/bin/python

import lywsd02
from datetime import datetime
import sys
from colors import bcolors as c

args = sys.argv
label = args[1]

print(f"Getting data from " + label + "... ",end="")

if label == 'cuarto':
    mac = 'A4:C1:38:13:F2:58'
elif label == 'salon':
    mac  = 'A4:C1:38:DB:57:38'
elif label == 'balcon':
    mac = 'A4:C1:38:BE:49:6F'

S = lywsd02.Lywsd02Client(mac)

try:
    data = S.data
    now = datetime.now()
    dt = S.time[0] - now # current date and time
    timestr = now.strftime("%Y-%m-%d %H:%M:%S")
except:
    print(f"{c.FAIL}ERROR getting data{c.ENDC}")
    # Do not write a line, stop function and return error code 1
    pass
    #raise Exception('Error getting data.')
    sys.exit(1)

#print(f'Time: {timestr}\nTemperature: {data.temperature:2.2f}º\nHumidity: {data.humidity:4.0f}%\nBattery: {data.battery:4.1f}%\nClock delay: {dt.total_seconds():9.2f} s')

f = open(label + '_temp.csv','a')
f.write(f'{timestr},{data.temperature:2.2f},{data.humidity:4.0f},{data.battery:4.1f},{dt.total_seconds():9.2f}\n')
f.close()

print(f"{c.OKGREEN}OK{c.ENDC}")
