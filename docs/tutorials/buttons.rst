Buttons
*****************

The device has eight buttons, arranged into two crosses, that can be used to
control the code running on it. The buttons are connected to GPIO pins on one
end, and to GND on the other, and they are scanned in the background by the
``gamepad`` module. The state of the buttons can be accessed with the
``badge.keys()`` function.

Example1: simplebuttons.py
=======

The following example uses a button press to turn a pixel on and off (by changing pixel's brightness to highest or lowest)::

    import badge

    badge.init()

    up = badge.K_UP
    down = badge.K_DOWN

    screen = badge.Pix()
    brightness = 16

    while True:
        badge.tick(0.2)
        key_pressed = badge.keys()
        if key_pressed == up:
            brightness = 16
        elif key_pressed == down:
            brightness = 0
        screen.pixel(0, 0, brightness)
        badge.show(screen)

There are eight buttons on the badge::

    badge.K_UP
    badge.K_LEFT
    badge.K_DOWN
    badge.K_RIGHT
    
    badge.K_S
    badge.K_O
    badge.K_X
    badge.K_Z

Other Examples
=======

buttonsmovepixels.py
The above example uses all eight buttons to move two pixels around the screen.
