namespace SpriteKind {
    export const NPC = SpriteKind.create()
    export const time_Machine = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.time_Machine, SpriteKind.Player, function (sprite, otherSprite) {
    Time_Machine = sprites.create(assets.image`adam baba ki time machine`, SpriteKind.time_Machine)
    sprites.destroyAllSpritesOfKind(SpriteKind.NPC)
    sprites.destroyAllSpritesOfKind(SpriteKind.time_Machine)
    music.play(music.melodyPlayable(music.buzzer), music.PlaybackMode.UntilDone)
    music.play(music.melodyPlayable(music.beamUp), music.PlaybackMode.InBackground)
    scene.setBackgroundImage(assets.image`Wormhole`)
    game.showLongText("STRAIGHT TO THE FUTURE IN 2050", DialogLayout.Bottom)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.createSoundEffect(WaveShape.Sawtooth, 1406, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.createSoundEffect(WaveShape.Noise, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
})
sprites.onOverlap(SpriteKind.NPC, SpriteKind.Player, function (sprite, otherSprite) {
    MAIN_CHARECTER.setPosition(82, 39)
    game.setDialogTextColor(2)
    game.showLongText("\"HI adventurer, I have a really important task for you!!!", DialogLayout.Bottom)
    MAIN_CHARECTER.setPosition(43, 48)
    game.showLongText("I have a time machine. You need to go in future to know our world there.   ", DialogLayout.Bottom)
    game.showLongText("Move left to time travel in the future.", DialogLayout.Bottom)
})
let MAIN_CHARECTER: Sprite = null
let Time_Machine: Sprite = null
scene.setBackgroundImage(assets.image`start`)
music.play(music.createSong(hex`0078000408040200001c00010a006400f401640000040000000000000000000000000005000004060014001800011e06001c00010a006400f401640000040000000000000000000000000000000002740000000400012a0400080001220c001000021e2914001800012418001c00012a1c00200002192524002800021e242c003000021e2934003800021e273c004000021e2940004400012448004c00021e275000540002192758005c0001205c006000012a60006400012468006c000122700074000119`), music.PlaybackMode.LoopingInBackground)
game.setDialogTextColor(9)
game.splash("BIO OICONOMOS")
game.splash("BY HYPER CODERS ")
game.setDialogTextColor(6)
game.showLongText("This game is made to spread awareness about bio diversity.     Press A to continue.", DialogLayout.Center)
game.showLongText("USE ARROW KEYS TO MOVE.      USE \"A\"and \"B\" TO INTERACT WITH OBJECTS.", DialogLayout.Center)
game.showLongText("DO YOU WANT TO START THE ADVENTURE? PRESS \"A\" TO CONTINUE.", DialogLayout.Full)
music.stopAllSounds()
game.setDialogTextColor(2)
scene.setBackgroundImage(assets.image`labh`)
Time_Machine = sprites.create(assets.image`adam baba ki time machine`, SpriteKind.time_Machine)
Time_Machine.setPosition(18, 53)
let SCIENTIST = sprites.create(assets.image`Scientist`, SpriteKind.NPC)
SCIENTIST.y = 32
MAIN_CHARECTER = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(MAIN_CHARECTER, 44, 47)
