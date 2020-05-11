# same as opencv-codereader.py module but uses picamera instead of cv2 to get image
# works with raspberry pi and camera extension

from PIL import Image
from picamera import PiCamera
import pyzbar.pyzbar as pyzbar
import time

from openclose import opener
from openclose import closer

# using picamera instead of cv2
picam = PiCamera()
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
        # get image
        picam.capture('capture.jpg')
        # grab that image
        frame =  Image.open("capture.jpg")
        # decode image
        decodedObjects = pyzbar.decode(frame)
        passCode = ''


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