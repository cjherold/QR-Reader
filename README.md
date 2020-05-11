### Dependencies
zbar is needed for pyzbar <br>
install zbar with homebrew https://brew.sh<br>
instructions found on website.
```bash
brew install zbar

pip3 install pyzbar
pip3 install opencv-python
```
### Raspberry Pi Version
raspberry pi version has a few others <br>
```bash
pip3 install Pillow
pip3 install PiCamera
```

### Run
Choose and run:<br>
python3 opencv-codereader.py<br>
or<br>
python3 picamera-codereader.py<br>


### Password Creation
create your own password on this website
https://www.the-qrcode-generator.com/

### Code png Files
show the Correct-password.png code to camera to open<br>
show the Incorrect-password.png code to camera to just print the code's contents (does not open because it doesn't match password)