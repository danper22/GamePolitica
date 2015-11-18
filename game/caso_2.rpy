define l = Character(_("Juliana"), color = "#3263D5")


init python:
    def stats_frame(name, hp, maxhp, **properties):

        ui.frame(xfill=False, yminimum=None, **properties)

        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)

        ui.text(name, size=20)

        ui.hbox() # "HP" from bar
        ui.text("Intentos", size=20)
        ui.bar(maxhp, hp,
               xmaximum=150)

        ui.close()
        ui.close()

        ui.vbox() # Level from (hp/maxhp)

        #ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)

        ui.close()
        ui.close()
        
image bg oficina2:
    "oficina2.jpg"
    size(config.screen_width, config.screen_height)

label fight_2(php=3):
    $ stats_frame(username, int(php), 3, xalign=.02, yalign=.05)
    return

image secretary women3:
    "secretaria2.png"
    size(265, 410)
#end characters

label caso_2:
    scene bg oficina2
    play music "musicSayonara.mp3"
    show secretary women3 at left
    l "Hola soy Juliana Murillo sere tu asistente en esta empresa llamada \"Jacky´s\" fundada en 2004"
    l "Jacky´s es una empresa enfocada en el negocio de bebidas gaseosas en Colombia, buscando satisfacer las necesidades de aquellos usuarios que no tienen definida una marca de bebida favorita"
    l "Gracias al sabor llamativo que jacky's ofrecia, resaltaba sobre la competencia, convirtiendose asi en la marca lider del marcado en Colombia durante un tiempo"
    l "La empresa quiso reducir los costos de produccion, cambiando asi sus proveedores por unos mas economicos, pero hace poco sus ganancias empezaron a disminuir quedando atras de su competencia."
    l "Los dueños de la empresa creen que el cambio de gerente es necesario, por lo tanto los propietarios de jacky´s quieren que seas el nuevo gerente"
    l "Tu misión, si decides aceptarla, es llevar las riendas de Jacky´s y encaminarla hacia el éxito"
    menu:
        "Acepto":
            $ vidas = 3
            $ Caso2_crisis1_sol = False
            $ Casos2_crisis2_sol = False
            $ Casos2_crisis3_sol = False
            $ Casos2_crisis4_sol = False
            jump iniciar_caso1
        "Deseo mirar otras empresas":
            jump start_2

label iniciar_caso2:
    if Casos2_crisis1_sol and Casos2_crisis2_sol and Casos2_crisis3_sol and Casos2_crisis4_sol:
        l "Felicidades la empresa ha atrevasado todas estas crisis gracias a tus acertadas decisiones"
        return
    call fight_2(vidas)# from _call_fight_1
    if vidas == 0:
        l "Has perdido"
        return
    
    user "Que hay pendiente por hacer?"
    
    #window hide None
    #call screen caso_1_imagemap
    #window show None
    call fight_2(vidas)
    l "Si %(username)s actualmente tenemos los siguientes problemas"
    
    $ opcion = 0
    $ Caso2_cual_crisis = 0
    menu:
        "Cambio de sabor":
            if Caso2_crisis1_sol is False:
                $ Caso2_cual_crisis = 1
                jump Caso2_crisis_1
         
label Caso2_crisis_1:
    if opcion == 0:
        l "%(username)s uno de los principales factores que  esta influyendo en esta crisis, es el cambio drastico de sabor que esta ofreciendo en estos momentos la empresa..."
        l "... Con esto, estamos perdiendo una ventaja competetiva que teniamos sobre los demas"
        l "Tu trabajo aqui %(username)s es tomar una la mejor decision para corregir esto ? "
        menu:
            "Aumentar salario de trabajadores actuales":
                jump aumentar_salario
            "Adquirir nuevamente los servicios de los antiguos proveedores":
                jump provecho_estaciones
            "Crear una nueva formula":
                jump cobertura_cambiaria
    if opcion == 1 or opcion == 2:
        l "Lo siento, la decisión tomada para hacer frente a la revaluación del peso ha sido fallida"
        $ vidas = vidas - 1
    else:
        l "Muy bien, el objetivo principal de la cobertura cambiaria es brindar certidumbre financiera para hacer frente a los compromisos en moneda extranjera."
        l "Gracias a esto la revaluación no tuvo mayor impacto en la empresa."
        $ Caso2_crisis1_sol = True
    jump iniciar_caso2

    
label aumentar_salario:
    l "Si tomas esta decision el salario de los trabajadores subira, para asi motivarlos a que hagan un sabor igual al de antes"
    l "Deseas tomar esta opción?"
    menu:
        "Si":
            $ opcion = 1
        "No":
            user "Me podrias repetir las opciones"
    if Caso2_cual_crisis == 1:
        jump Caso2_crisis_1
    elif Caso2_cual_crisis == 2:
        jump Caso2_crisis_2
    elif Caso2_cual_crisis == 3:
        jump Caso2_crisis_3
    elif Caso2_cual_crisis == 4:
        jump Caso2_crisis_4