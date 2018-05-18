import RPi.GPIO as GPIO
from time import sleep

PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

print('Now start to test GPIO Input')
count = 0
try:
    while True:
        if GPIO.input(PIN) == 0:
            count += 1
            print('Button On:{}'.format(count))
        sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
