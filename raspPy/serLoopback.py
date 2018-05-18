import serial
ser = serial.Serial('/dev/ttyS0', 115200)
ser.flushInput()

try:
    while True:
        c = ser.read()
        ser.write(c)
        print(c)
        if c == b'x':
            break
except KeyboardInterrupt:
    ser.close()

    
