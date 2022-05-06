def on_button_pressed_a():
    basic.set_led_color(0x007fff)
    basic.show_icon(IconNames.DUCK, 1000)
input.on_button_pressed(Button.A, on_button_pressed_a)
