# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

image bg oficina1:
    "oficina1.jpg"
    size(config.screen_width, config.screen_height)

image secretary women1:
    "secretaria1.png"
    size(265, 410)

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define e = Character('Daniela Perez', color="#c8ffc8")

init python:
    casos = [
        ("caso_1", _("Cultivos SAYONARA"), "1"),
        ("caso_2", _("Caso 2 - RAMO"), "2"),
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
    show secretary women1 at right
    with dissolve
    e "Hola, bienvenido a (Nombre del juego) Donde ayudamos a diferentes empresas a salir de diferentes crisis."
    
    
    window show
    
    e "A continuacion tendras que escoger una de las siguientes empresas de la cual te haras cargo como gerente de ella."
    e "Antes de empezar necesitaremos tu nombre"
    
    $ username = ""
    $ user = DynamicCharacter("username", color=(192, 64, 64, 255))
    $ username = renpy.input("Tu nombre")
    #user "%(username)s."
    e "Mucho gusto %(username)s."
    e "Listo empecemos por favor escoge una de estas empresas"
    
    $ casos_adjustment = ui.adjustment()
    call screen casos(adj = casos_adjustment)
    
    if _return is False:
        jump end
    
    call expression _return
    return
    
label start_2:
    $ casos_adjustment = ui.adjustment()
    call screen casos(adj = casos_adjustment)
    
    if _return is False:
        jump end
    
    call expression _return
    return
    
label end:
    e "Fin"
    return