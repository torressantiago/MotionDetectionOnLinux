#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
import time

ADAFRUIT_IO_USERNAME = "torres_santiago"
ADAFRUIT_IO_KEY = "aio_IHir43lNkCvWncShzIbKifb7nebk"


# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


try: # if we have a 'kill' feed
    kill = aio.feeds('kill')
except RequestError: # create a cpup feed
    feed = Feed(name="kill")
    kill = aio.create_feed(feed)


#Master = aio.feeds('Master')
#feed = Feed(name="Master")

while True:
    data = aio.receive(kill.key)
    if data.value == "ON":
        print('received <- ON\n')
    elif data.value == "OFF":
        print('received <- OFF\n')

    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.5)