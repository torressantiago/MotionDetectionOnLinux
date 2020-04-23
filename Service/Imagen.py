#!/usr/bin/python3.7
from Adafruit_IO import Client, Feed, RequestError
import base64
import cv2 as cv
import time

 
ADAFRUIT_IO_USERNAME = "torres_santiago"
ADAFRUIT_IO_KEY = "aio_IHir43lNkCvWncShzIbKifb7nebk"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


try: # if we have a 'vidfeed' feed
    vidfeed = aio.feeds('vidfeed')
except RequestError: # create a cpup feed
    feed = Feed(name="vidfeed")
    vidfeed = aio.create_feed(feed)

i = 0

t1 = time.perf_counter()
t2 = t1

while True:
    t2 = time.perf_counter()
    if t2-t1 > 30:
        t1 = t2
        # create an in-memory file to store raw image data
        webcam = cv.VideoCapture(-1) #Add proper number for device
        for i in range(100):
            _,frame = webcam.read() 
        
        # write camera data to the stream (file)
        stream = "FrameActu.jpg"
        cv.imwrite(filename=stream,img=frame)
        webcam.release()
        cv.destroyAllWindows()

        base = '/home/pi/Desktop/'
        src = base + stream

        with open(src, "rb") as imageFile:
            string = (base64.b64encode(imageFile.read()).decode("ascii"))
            aio.send('vidfeed', string )
            print("OK!")

"""
base = '/home/pi/Desktop/'
src = base + 'FrameActu.jpg' 

with open(src, "rb") as imageFile:
    string = (base64.b64encode(imageFile.read()).decode("ascii"))
    aio.send('vidfeed', string )
"""