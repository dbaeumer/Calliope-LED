input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
})
led.setDisplayMode(DisplayMode.Greyscale)
led.plot(1, 1)
led.plot(2, 0)
basic.forever(function () {
	
})
