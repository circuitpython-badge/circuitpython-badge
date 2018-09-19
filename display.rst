Buttons
*****************

The device has eight buttons, arranged into two crosses, that can be used to
control the code running on it. The buttons are connected to GPIO pins on one
end, and to GND on the other, and they are scanned in the background by the
``gamepad`` module. The state of the buttons can be accessed with the
``badge.keys()`` function.


Example
=======

