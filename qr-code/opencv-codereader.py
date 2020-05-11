# Uses computer's camera to read qr code

import cv2
import pyzbar.pyzbar as pyzbar
import time

from openclose import opener
from openclose import closer

# start grabbing images from camera. number is which cam device you want to use
# if None type object error try changing VideoCapture(0) or VideoCapture(1)
cap = cv2.VideoCapture(1)
# true = open lock
lockState = True

def openLock():
    """Uses the opener module to test or open the lock"""
    opener.open()
    # opener.pi_open() 

def closeLock():
    """Uses the closer module to test or open the lock"""
    closer.close()
    # closer.pi_close()


def lookForCode(lockState):
    """This runs a loop that watches for a specific qrcode.
       If found it opens/closes the lock and returns the state."""

    while True:
        _, frame = cap.read()

        passCode = ''
        decodedObjects = pyzbar.decode(frame)
        # needs to check all recent frames
        for each in decodedObjects:
            # get b'Correct qr password'
            passCode = str(each.data)
            # trim from b'Correct qr password' to Correct qr password
            passCode = passCode[2:-1]
            print(passCode)
        
        # show indication that code is running
        print('.........')

        # if code is correct, open or close...also decodedObjects have a b stuck to the beginning
        if passCode == 'Correct qr password':
            print('\tData: ', passCode)
            print('\tPassword match success!')

            if lockState:
                closeLock()
                lockState = False
                break #return new state, sleep, then run this function again
            else:
                openLock()
                lockState = True
                break #return new state, sleep, then run this function again

        # framerate: how fast it loops and watches for code
        time.sleep(.5)

    return lockState


# main function that runs when calling this module
if __name__ == '__main__':
    while True:
        print('=================================================')
        # pass in the state of the lock (open or closed as true or false)
        # then it watches until the password is found and then returns the new state
        lockState = lookForCode(lockState)
        print('\tLock=', lockState)

        # sleeps while opening/closing lock
        time.sleep(4)