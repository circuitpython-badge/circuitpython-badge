Accelerometer
*****************

There is a LIS3DH accelerometer in the middle of the board, under the display,
which can be used to read the position and movement of the device. It is also
connected over an I²C protocol to the ``board.SDA0`` and ``board.SCL0`` pins.
It can be accessed with the ``badge.accel()`` function.


Examples
=====

