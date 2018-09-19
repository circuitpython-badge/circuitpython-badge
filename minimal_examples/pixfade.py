''' 
circuitpython-badge/minimal_examples/pixfade.py

A basic example using loops to fade all the leds on the badge :D

'''

import badge
import random

badge.init()

p = badge.Pix()

def fadeinout():
    # f is the current step brightness and x/y to set LED in the grid:
    for f in range(10):
        for x in range(p.width):
            for y in range(p.height):
                p.pixel(x, y, f)
        badge.show(p)
        badge.tick(0.01)
                
    for f in range(10):
        for x in range(p.width):
            for y in range(p.height):
                p.pixel(x, y, 9-f)
        badge.show(p)
        badge.tick(0.01)

# if you want to fade in and out once:

fadeinout()

# If you want to run the fade in a loop, uncomment the lines below:
    
#while True:
#    fadeinout()

# Alternatively import pixfade and use pixfade.fadeinout()
