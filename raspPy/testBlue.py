import serial
port = '/dev/rfcomm0'
ser = serial.Serial(port, 115200)
# ser = serial.Serial('/dev/ttyAMA0', 115200)
print('serial Port:{}'.format(port))
ser.flushInput()
arr = bytearray('Now start Bluetooth test', 'utf-8')
ser.write(arr)
try:
    while True:
        c = ser.read()
        ser.write(c)
        print(c)
        if c == b'x':
            break
except KeyboardInterrupt:
    ser.close()
