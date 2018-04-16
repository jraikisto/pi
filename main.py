#!/usr/bin/env python3

from time import sleep
from random import randint
import unicornhat as unicorn
from weather import Weather
from pics import Pics
import math

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.175)
uh_width,uh_height=unicorn.get_shape()

def drawPic(pics):
    pic1 = pics[0]
    pic2 = pics[1]
    for h in range(uh_height):
        for w in range(uh_width):
            if w < 5:
                unicorn.set_pixel(w, h, pic1[h][w][0], pic1[h][w][1], pic1[h][w][2])
            else:
                unicorn.set_pixel(w, h, pic2[h][w][0], pic2[h][w][1], pic2[h][w][2])
    unicorn.show()

def weatherUpdate():
    weather = Weather()
    location = weather.lookup_by_location('tampere')
    condition = location.condition()
    return condition

nums = [Pics.one, Pics.two, Pics.three]
while True:
    for n in nums:
        for x in range(0, 99)
            wet = weatherUpdate()
            print(wet.text())
            drawPic(retNum(x, 255, 255, 255))
            sleep(1)
