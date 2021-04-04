import os, os.path
from picamera import PiCamera

dir = "./photos"
countofImages = len(next(os.walk(dir))[2]) 
print (countofImages)

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

camera.capture('./photos/image{0:04d}.jpg'.format(countofImages))
# camera.capture('image.jpg')
camera.stop_preview()
print("Done")  