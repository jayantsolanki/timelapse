import os, os.path
from picamera import PiCamera
import datetime

dir = "./photos"
dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
countofImages = len(next(os.walk(dir))[2]) 

print("RPi took next photo for yuour timelapse: " + datetimeformat)
print ('Total Images captured {d}'.format(countofImages+1))

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

camera.capture('./photos/image{0:06d}.jpg'.format(countofImages))
# camera.capture('image.jpg')
camera.stop_preview()
print("Done")  
