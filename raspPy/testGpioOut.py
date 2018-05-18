import RPi.GPIO as GPIO
from time import sleep

PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
print('Now start to test GPIO')
try:
    while True:
        GPIO.output(PIN,1)
        print('High')
        sleep(0.5)
        GPIO.output(PIN,0)
        print('Low')
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
