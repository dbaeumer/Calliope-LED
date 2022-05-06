def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.A, on_button_pressed_a)

led.set_display_mode(DisplayMode.GREYSCALE)
led.plot(1, 1)
led.plot(2, 0)

def on_forever():
    pass
basic.forever(on_forever)
