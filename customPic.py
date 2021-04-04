import os, os.path
from picamera import PiCamera
import datetime

dir = "/home/pi/timelapse/timelapse/photos"
dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
countofImages = len(next(os.walk(dir))[2]) 

print("RPi took next photo for your timelapse: " + datetimeformat)
print ('Total Images captured {0}'.format(countofImages+1))

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

camera.capture('/home/pi/timelapse/timelapse/photos/image{0:04d}.jpg'.format(countofImages))
camera.stop_preview()
print("Done")  
