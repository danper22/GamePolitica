# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

image bg oficina1:
    "oficina1.jpg"
    size(800, 600)

image secretaria1:
    "secretaria1.png"
    size(265, 410)

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define e = Character('La secre', color="#c8ffc8")

init python:
    casos = [
        ("caso_1", _("Caso 1"), "Mierda"),
        ("caso_2", _("Caso 2 - RAMO"), "RAMO"),
    ]

screen casos:
    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for label, name, ver in casos:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True

                        hbox:
                            text name style "button_text" min_width 420
                            text ver style "button_text"

                null height 20

                textbutton _("Salir"):
                    xfill True
                    action Return(False)

        bar adjustment adj style "vscrollbar"

# The game starts here.
# - El juego comienza aquí.
label start:
    scene bg oficina1
    show secretaria1
    with dissolve
    e "Hola"
    
    window show
    
    e "Bienvenido"
    
    $ username = ""
    $ user = DynamicCharacter("username", color=(192, 64, 64, 255))
    $ username = renpy.input("Tu nombre")
    user "Hola soy %(username)s."
    e "Ok"
    
    $ casos_adjustment = ui.adjustment()
    call screen casos(adj = casos_adjustment)
    
    if _return is False:
        jump end
    
    call expression _return
    return
    
label end:
    e "Fin"
    return