def on_b_pressed():
    music.play(music.create_sound_effect(WaveShape.SAWTOOTH,
            1406,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    music.play(music.create_sound_effect(WaveShape.NOISE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

scene.set_background_image(assets.image("""
    start
"""))
music.play(music.create_song(hex("""
        006e000408020206001c00010a006400f401640000040000000000000000000000000000000002480000000400012a08000c00012210001400011d14001800011e18001c00011920002400011e24002800012728002c00031b242a30003400012538003c00041b20252a3c00400002222909010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8002b000000010001070800090001071000110001041400150002060818001900010a1c001d000108200021000109
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.set_dialog_text_color(9)
game.splash("BIO OICONOMOS")
game.splash("BY HYPER CODERS ")
game.set_dialog_text_color(6)
game.show_long_text("This game is made to spread awareness about bio diversity.     Press A to continue",
    DialogLayout.CENTER)
game.show_long_text("USE ARROW KEYS ↑↓→← TO MOVE.      USE \"A\"and \"B\" TO INTERACT WITH OBJECTS",
    DialogLayout.CENTER)
game.show_long_text("DO YOU WANT TO START THE ADVENTURE? PRESS \"A\" TO CONTINUE.",
    DialogLayout.FULL)
music.stop_all_sounds()
game.set_dialog_text_color(2)
scene.set_background_image(assets.image("""
    labh
"""))
MAIN_CHARECTER = sprites.create(img("""
        . . . . f f f f . . . . . 
            . . f f f f f f f f . . . 
            . f f f f f f c f f f . . 
            f f f f f f c c f f f c . 
            f f f c f f f f f f f c . 
            c c c f f f e e f f c c . 
            f f f f f e e f f c c f . 
            f f f b f e e f b f f f . 
            . f 4 1 f 4 4 f 1 4 f . . 
            . f e 4 4 4 4 4 4 e f . . 
            . f f f e e e e f f f . . 
            f e f b 7 7 7 7 b f 1 f . 
            e 4 f 7 7 7 7 7 7 f 4 e . 
            e e f 6 6 6 6 6 6 f e e . 
            . . . f f f f f f . . . . 
            . . . f f . . f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(MAIN_CHARECTER, 44, 47)