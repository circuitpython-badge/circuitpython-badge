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
