scene.set_background_color(2)
scene.set_background_image(assets.image("""
    monstre
"""))
jugador_principal = sprites.create(assets.image("""
        jugador principal
    """),
    SpriteKind.player)
controller.move_sprite(jugador_principal)