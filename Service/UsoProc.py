#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import time

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_USERNAME = "torres_santiago"
ADAFRUIT_IO_KEY = "aio_IHir43lNkCvWncShzIbKifb7nebk"


# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

"""
try: # if we have a 'cpup' feed
    cpup = aio.feeds('cpup')
except RequestError: # create a cpup feed
    feed = Feed(name="cpup")
    cpup = aio.create_feed(feed)
"""  

cpup = aio.feeds('cpup')
feed = Feed(name="cpup")

#feed = Feed(name="Calles")

i = 0

t1 = time.perf_counter()
t2 = t1

while True:
    t2 = time.perf_counter()
    if t2-t1 > 5:
        t1 = t2
        a = psutil.cpu_percent()
        aio.send("cpup", a)
