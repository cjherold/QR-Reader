# This is the code to open the lock using a servo
# open() is used for testing and prints only
# pi_open() uses raspberry pi to turn servo

# import RPi.GPIO as GPIO
import time

def open():
    """Just prints Opening, used for testing"""
    print('\n\tOpening')

def pi_open():
    """Turns servo from closed to open position (door lock)"""
    print("\nOpening lock :)")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    servo1 = GPIO.PWM(11, 50)

    # start(0) pulse off
    print('servo.start(0)')
    servo1.start(0)
    time.sleep(1)

    # turns a little at a time using servo
    print('turning...')
    i = 2
    while i < 8.5:
        # pulse next degree 
        print('ChangeDutyCycle(%d)' % i)
        servo1.ChangeDutyCycle(i)
        time.sleep(0.2)
        # no pulse, this should help turn smoother
        servo1.ChangeDutyCycle(0)
        time.sleep(0.1)
        i += 1

    # stop pulse
    print('servo.ChangeDutyCycle(0)')
    servo1.ChangeDutyCycle(0)
    servo1.stop()
    GPIO.cleanup()
    print('done opening')

if __name__ == '__main__':
    open()