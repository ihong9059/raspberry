# import smbus, time
#
# bus = smbus.SMBus(1)
# i2cAddr = 0x68
#
# bus.write_byte_data(i2cAddr, 0x06, 0)
# a = bux.read_byte_data(i2cAddr, 0x38)
#
# def ScaleValue(val):
#     if val >= 32768:
#         val = val - 65536
#     return val
#
# count = 0
# try:
#     while True:
#         print('count:{}'.format(count))
#         count += 1
#         time.sleep(1)
# except KeyboardInterrupt:
#     bus.close()
#

import smbus
import time

bus = smbus.SMBus(1)
# I2C address for MMA7660
addr = 0x50
# addr = 0xA0
# addr = 0x4C
try:
    bus.write_byte_data(addr, 0x00, 0x55)
    time.sleep(0.25)
except :
    print('Error in i2c write')

while True:
    try:
        x = bus.read_byte_data(addr,0x00)
        print(x)
        time.sleep(0.25)
    except:
        print( 'exiting...')
        break
