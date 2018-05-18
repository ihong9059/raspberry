import RPi.GPIO as GPIO
from time import sleep

PIN = 12

pwm_duty = 0
pwm_freq = 5000

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

p = GPIO.PWM(PIN, pwm_freq)
p.start(pwm_duty)

print('Now start to test GPIO PWM')

try:
    while True:
        p.ChangeDutyCycle(pwm_duty)
        pwm_duty += 1
        if pwm_duty > 100:
            pwm_duty = 0
        print('pwm:{}'.format(pwm_duty))
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
