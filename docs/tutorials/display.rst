Display
*****************

There is a display of 14×11 red pixels on the device, controlled by a
IS31FL3733 chip connected over an I²C bus to the ``board.SDA0`` and
``board.SCL0`` pins. It can be accessed with the ``badge.show()`` function and
its brightness can be adjusted with the ``badge.brightness()`` function. It's
capable of displaying 256 shades of red, however, since most of those shades
are very similar, the library selects only 16 distinct shades that you can use.

Example 1: twopixels.py
=============

The following example creates two pixels on the screen::

    import badge

    badge.init()

    screen = badge.Pix()
    screen.pixel(3, 3, 10)
    screen.pixel(10, 7, 10)
    badge.show(screen)

The main function being used in this example is::

    badge.Pix().pixel(WIDTH, HEIGHT, BRIGHTNESS)

Choose a WIDTH between 0 and 13, a HEIGHT between 0 and 10, and a brightness between 0 and 15.

Your chosen pixels will not show up on the screen until you use::

    badge.show()

Example 2: pixfade.py
=============

The following example uses loops to fade all the leds on the badge::

    import badge
    import random

    badge.init()

    screen = badge.Pix()

    def fadeinout():
        # f is the current step brightness and x/y to set LED in the grid:
        for f in range(10):
            for x in range(14):
                for y in range(11):
                    screen.pixel(x, y, f)
            badge.show(screen)
            badge.tick(0.01)

        for f in range(10):
            for x in range(14):
                for y in range(11):
                    screen.pixel(x, y, 10-f)
            badge.show(screen)
            badge.tick(0.01)

    fadeinout()

To create a delay of 0.2 seconds in the loop, this example uses::

    badge.tick(0.2)

This has the same function as::

    time.sleep(0.2)

but removes the need to import time.
