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

The following example turns on two leds on the badge::

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

    badge.init()

    screen = badge.Pix()
    
    def fadeinout():
        # f is the current step brightness and x/y to set LED in the grid:
        for f in range(screen.height):
            for x in range(screen.width):
                for y in range(screen.height):
                    screen.pixel(x, y, f)
            badge.show(screen)
            badge.tick(0.01)

        for f in range(screen.height):
            for x in range(screen.width):
                for y in range(screen.height):
                    screen.pixel(x, y, 10-f)
            badge.show(screen)
            badge.tick(0.01)

    fadeinout()

To create a delay of 0.2 seconds in the loop, this example uses::

    badge.tick(0.2)

This has the same function as::

    time.sleep(0.2)

but removes the need to import time.

Example 3: blitscrollingtext.py
=============

The following example scrolls text across the badge::

    import badge

    badge.init()

    text = badge.Pix.from_text('Hello badge!')

    screen = badge.Pix()

    # Start the text just off the right side of the screen
    x_pos = screen.width
    y_pos = 3       # 3 pixels below the top of the screen to improve formatting

    while True:
        badge.tick(0.2)

        # Move the text left, until it's completely off the screen
        x_pos -= 1
        if x_pos < -text.width:
            x_pos = screen.width

        # Draw the text onto the screen in its current position
        screen.blit(text, x_pos, y_pos)

        badge.show(screen)

This introduces two new methods, firstly::

    text = badge.Pix.from_text('Hello badge!')

This allows you to chose the text to be scrolled.

Secondly::

    screen.blit(IMAGE, POS_X, POS_Y)

Specify an image (or in the above example, our text), to be drawn on the given position on the screen.
