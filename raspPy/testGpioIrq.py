import RPi.GPIO as GPIO
from time import sleep

def KeyHandler(n):
    print("Key is pressed[%d]" %n)

PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

GPIO.add_event_detect(PIN, GPIO.FALLING, callback=KeyHandler)

print('Now start to test GPIO Input')
count = 0
try:
    while True:
        print('sec:{}'.format(count))
        count += 1
        sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
