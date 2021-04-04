import os, os.path
from picamera import PiCamera

dir = "./photos"
countofImages = len(next(os.walk(dir))[2]) #dir is your directory path as string
print (countofImages)
# print('image{0:04d}.jpg'.format(countofImages))
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

camera.capture('image{0:04d}.jpg'.format(countofImages))
# camera.capture('image.jpg')
camera.stop_preview()
print("Done")  