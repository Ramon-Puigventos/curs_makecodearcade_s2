scene.setBackgroundColor(2)
scene.setBackgroundImage(assets.image`monstre`)
let jugador_principal = sprites.create(assets.image`jugador principal`, SpriteKind.Player)
controller.moveSprite(jugador_principal)
