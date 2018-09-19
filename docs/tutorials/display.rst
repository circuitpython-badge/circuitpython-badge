Display
*****************

There is a display of 14×11 red pixels on the device, controlled by a
IS31FL3733 chip connected over an I²C bus to the ``board.SDA0`` and
``board.SCL0`` pins. It can be accessed with the ``badge.show()`` function and
its brightness can be adjusted with the ``badge.brightness()`` function. It's
capable of displaying 256 shades of red, however, since most of those shades
are very similar, the library selects only 16 distinct shades that you can use.


Examples
=============

