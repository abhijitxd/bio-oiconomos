@namespace
class SpriteKind:
    NPC = SpriteKind.create()
    time_Machine = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Time_Machine
    Time_Machine = sprites.create(assets.image("""
            adam baba ki time machine
        """),
        SpriteKind.time_Machine)
    sprites.destroy_all_sprites_of_kind(SpriteKind.NPC)
    sprites.destroy_all_sprites_of_kind(SpriteKind.time_Machine)
    music.play(music.melody_playable(music.buzzer),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.melody_playable(music.beam_up),
        music.PlaybackMode.IN_BACKGROUND)
    scene.set_background_image(assets.image("""
        Wormholes
    """))
    game.show_long_text("STRAIGHT TO THE FUTURE IN 2050", DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.time_Machine, SpriteKind.player, on_on_overlap)

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

def on_on_overlap2(sprite2, otherSprite2):
    MAIN_CHARECTER.set_position(82, 39)
    game.set_dialog_text_color(2)
    game.show_long_text("\"HI adventurer, I have a really important task for you!!!",
        DialogLayout.BOTTOM)
    MAIN_CHARECTER.set_position(43, 48)
    game.show_long_text("I have a time machine. You need to go in future to know our world there.   ",
        DialogLayout.BOTTOM)
    game.show_long_text("Move left to time travel in the future.",
        DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.NPC, SpriteKind.player, on_on_overlap2)

MAIN_CHARECTER: Sprite = None
Time_Machine: Sprite = None
scene.set_background_image(assets.image("""
    start
"""))
music.play(music.create_song(hex("""
        0078000408040200001c00010a006400f401640000040000000000000000000000000005000004060014001800011e06001c00010a006400f401640000040000000000000000000000000000000002740000000400012a0400080001220c001000021e2914001800012418001c00012a1c00200002192524002800021e242c003000021e2934003800021e273c004000021e2940004400012448004c00021e275000540002192758005c0001205c006000012a60006400012468006c000122700074000119
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.set_dialog_text_color(9)
game.splash("BIO OICONOMOS")
game.splash("BY HYPER CODERS ")
game.set_dialog_text_color(6)
game.show_long_text("This game is made to spread awareness about Bio Diversity and our Enviroment.     Press A to continue.",
    DialogLayout.CENTER)
game.show_long_text("USE ARROW KEYS TO MOVE.      USE \"A\"and \"B\" TO INTERACT WITH OBJECTS.",
    DialogLayout.CENTER)
game.show_long_text("DO YOU WANT TO START THE ADVENTURE? PRESS \"A\" TO CONTINUE.",
    DialogLayout.FULL)
music.stop_all_sounds()
game.set_dialog_text_color(2)
scene.set_background_image(assets.image("""
    labh
"""))
Time_Machine = sprites.create(assets.image("""
        adam baba ki time machine
    """),
    SpriteKind.time_Machine)
Time_Machine.set_position(18, 53)
SCIENTIST = sprites.create(assets.image("""
    Scientistfi
"""), SpriteKind.NPC)
SCIENTIST.y = 32
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