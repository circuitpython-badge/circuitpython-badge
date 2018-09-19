Radio
*****************

There is an NRF24L01+ radio module on board, connected to the ``board.RADIO*``
pins. The connections are as follows:

    * ``RADIO0`` — ``CE``
    * ``RADIO1`` — ``CSN``
    * ``RADIO3`` — ``SCK``
    * ``RADIO4`` — ``MOSI``
    * ``RADIO5`` — ``MISO``

There are currently no built-in functions or libraries for handling the
communication with this module. And external library needs to be used.


Examples
=====

