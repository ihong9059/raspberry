import serial
import time
from threading import Thread, Lock

class serThread(Thread):
    writeFlag = True
    readFlag = False
    readStr = ''
    writeStr = 'Now Start Serial'
    newFrame = ''

    def __init__(self):
        print('Now Start SerialThread')
        Thread.__init__(self)

    def send(self, writeStr):
        self.writeStr = writeStr
        self.writeFlag = True
        print('ser write')

    def FileSave(self,filename,content):
        import io
        with open(filename, "a+") as myfile:
            myfile.write(content)

    def parseFrame(self, inFrame):
        first = inFrame.rfind('{')
        last = inFrame.rfind('}')
        if last > 150:
            print('Wrong Frame, clear buffer')
            self.readStr = ''
            return False
        elif last > first:
            self.newFrame = inFrame[first:last+1]
            self.readStr = ''
            return True
        else:
            print('Wrong Frame, clear buffer')
            self.readStr = ''
            return False


    def run(self):
        port = '/dev/ttyS0'
        # port = 'COM7'
        # port = 'COM38'
        count = 0
        with serial.Serial(port, 115200, timeout = 0) as ser:
            print('serial Port:{}'.format(port))
            while True:
                time.sleep(0.001)
                try:
                    bytesToRead = ser.inWaiting()
                    if bytesToRead:
                        sTemp = str(ser.read(bytesToRead),'utf-8')
                        # print(sTemp)
                        self.readStr += sTemp;
                        if bytesToRead == 1:
                            print(sTemp)
                        if self.readStr.find('}') != -1:
                            if self.parseFrame(self.readStr):
                                self.readStr = ''
                                self.newFrameFlag = True
                                print(self.newFrame)
                        self.readFlag = True
                except:
                    print('Error Data')

                if self.writeFlag:
                    ser.write(bytearray(self.writeStr,'utf-8'))
                    self.writeFlag = False

        print('End of inThread')

class testThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            pass
        print('End of testThread')

if __name__ == "__main__":
    testSer = serThread()
    testSer.start()
