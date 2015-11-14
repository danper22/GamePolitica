# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define e = Character('La secre', color="#c8ffc8")
image bg oficina1:
    "oficina1.jpg"
    size(800,600)
image secretaria normal = "secretaria.jpg"
    
# The game starts here.
# - El juego comienza aquí.

init python:    
    casos = [
        ("caso_1", _("El caso 1"), "1"),
        ("caso_2", _("El caso 2"), "2")
        ]


label start:
    
    scene bg oficina1
    show secretaria normal
    with dissolve
        
    e "Hola has sido elegido entre muchos candidatos para tomar las riendas de las siguientes empresas"

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    return
