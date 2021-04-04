from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

camera.capture('image.jpg')
camera.stop_preview()
print("Done")  
