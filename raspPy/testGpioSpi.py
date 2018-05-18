import spidev, time
spi = spidev.SpiDev()
spi.open(0,0)

spi.max_speed_hz = 1000000
spi.mode = 0

a = 0x00
b = 0x00

def FileSave(filename,content):
    import io
    with open(filename, "a+") as myfile:
        myfile.write(content)

from datetime import datetime
try:
    while True:
        a = a& ~0x80
        b = b& ~0x80
        readData = spi.xfer2([a,b])
        print('a:{}, b:{}'.format(a,b))
        dt = datetime.now()
        writeStr = 'Send:: ' + str(dt.date()) + ':' + str(dt.time())
        writeStr += '--->a:{}, b:{}'.format(a,b)
        FileSave('spi.txt', writeStr+'\n')
        print('readData:{}'.format(readData))
        writeStr = 'readData:{}'.format(readData)
        FileSave('spi.txt', writeStr+'\n')
        time.sleep(0.5)
        a += 1
        b += 1
except KeyboardInterrupt:
    spi.close()
