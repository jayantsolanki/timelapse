import os, os.path
from picamera import PiCamera
import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

dir = "/home/pi/timelapse/timelapse/photos"
font = ImageFont.truetype("DejaVuSans.ttf", 32)
fontsmall = ImageFont.truetype("DejaVuSans.ttf", 18)
fontcolor = (238,161,6)

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
countofImages = len(next(os.walk(dir))[2]) 

print("RPi took next photo for your timelapse: " + datetimeformat)
print ('Total Images captured {0}'.format(countofImages+1))

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
completeFilePath = '/home/pi/timelapse/timelapse/photos/image{0:04d}.jpg'.format(countofImages)

camera.capture(completeFilePath)

# get the timestamp drawing
splitup = datetimeformat.split("_")
date = splitup[0]
t = splitup[1][:]


img = Image.open(completeFilePath)
draw = ImageDraw.Draw(img)
draw.text((img.width-200,60), date, fontcolor, font = font)
draw.text((img.width-200,105), t, fontcolor, font = fontsmall)
img.save(completeFilePath)



camera.stop_preview()
print("Done")  
