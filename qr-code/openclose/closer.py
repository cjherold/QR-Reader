# This is the code to close the lock using a servo
# close() is used for testing and prints only
# pi_close() uses raspberry pi to turn servo

# import RPi.GPIO as GPIO
import time

def close():
    """Just prints Closing, used for testing"""
    print('\n\tClosing')

def pi_close():
    """Turns servo from open to closed position (door lock)"""
    print("\nClosing lock :(")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    servo1 = GPIO.PWM(11, 50)

    # start(0) pulse off
    print('servo.start(0)')
    servo1.start(0)
    time.sleep(1)

    # turns a little at a time using servo
    print('turning...')
    i = 8.5
    while i > 2:
        # pulse next degree 
        print('ChangeDutyCycle(%d)' % i)
        servo1.ChangeDutyCycle(i)
        time.sleep(0.2)
        # no pulse, for smoother turn
        servo1.ChangeDutyCycle(0)
        time.sleep(0.1)
        i -= 1

    # stop pulse
    print('servo.ChangeDutyCycle(0)')
    servo1.ChangeDutyCycle(0)
    servo1.stop()
    GPIO.cleanup()
    print('done closing')

if __name__ == '__main__':
    close()

