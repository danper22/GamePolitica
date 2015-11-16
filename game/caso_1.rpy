#begin characters
define l = Character(_("Esperanza"), color="#ffcccc")

screen caso_1_imagemap:
    imagemap:
        auto "imageMapSayonara_%s.jpg"

        hotspot (8, 200, 78, 78) action Return("swimming") alt "Swimming"
        hotspot (204, 50, 78, 78) action Return("science") alt "Science"
        hotspot (452, 79, 78, 78) action Return("art") alt "Art"
        hotspot (602, 316, 78, 78) action Return("go home") alt "Go Home"

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


        
label fight(php=3):
    $ stats_frame(username, int(php), 3, xalign=.02, yalign=.05)
    return

image secretary women2:
    "secretaria2.png"
    size(265, 410)
#end characters

label caso_1:
    play music "musicSayonara.mp3"
    show secretary women2 at left
    l "Hola soy Esperanza sere tu asistente en esta empresa llamada \"Cultivos SAYONARA\" fundada en 1990"
    l "SAYONARA es una empresa productora y comercializadora de flores en gran parte al exterior"
    l "La empresa se caracteriza por el buen ambiente laboral que se percibe en ella"
    l "Actualmente se tiene un buen margen de ganancias y un bajo nivel de endeudamiento"
    l "Tu misión, si decides aceptarla, es llevar las riendas de SAYONARA y encaminarla hacia el éxito"
    menu:
        "Acepto":
            $ vidas = 3
            $ crisis1_sol = False
            $ crisis2_sol = False
            $ crisis3_sol = False
            $ crisis4_sol = False
            jump iniciar_caso1
        "Deseo mirar otras empresas":
            jump start_2

label iniciar_caso1:
    if crisis1_sol and crisis2_sol and crisis3_sol and crisis4_sol:
        l "Felicidades la empresa ha atrevasado todas estas crisis gracias a tus acertadas decisiones"
        return
    call fight(vidas)# from _call_fight_1
    if vidas == 0:
        l "Has perdido por tu culpa la empresa quebro y me toca prostituirme para sostener mi hogar putoooo"
        return
    
    user "Que hay pendiente por hacer?"
    
    #window hide None
    #call screen caso_1_imagemap
    #window show None
    call fight(vidas)
    l "Si %(username)s actualmente tenemos los siguientes problemas"
    
    $ opcion = 0
    $ cual_crisis = 0
    menu:
        "Revaluacion del peso":
            if crisis1_sol is False:
                $ cual_crisis = 1
                jump crisis_1
            else:
                l "No te preocupes, este problema ya lo has solucionado."
                jump iniciar_caso1
        "Destrucción y pérdida de cultivos":
            if crisis2_sol is False:
                $ cual_crisis = 2
                jump crisis_2
            else:
                l "No te preocupes, este problema ya lo has solucionado."
                jump iniciar_caso1

label crisis_1:
    if opcion == 0:
        l "%(username)s la empresa se esta viendo afectada a causa del cambio de las condiciones macroeconomicas del pais y la llegada de la revaluación del peso"
        l "Por culpa de esto se disminuyeron notoriamente los margenes de ganancias, con un gran porcentaje de pérdida de rentabilidad"
        l "Debes tomar la mejor decisión para solucionar esto"
        menu:
            "Ampliacion del portafolio de productos":
                jump ampliacion_portafolio
            "Sacar provecho a las estaciones":
                jump provecho_estaciones
            "Cobertura cambiarias":
                jump cobertura_cambiaria
    if opcion == 1 or opcion == 2:
        l "Lo siento, la decisión tomada para hacer frente a la revaluación del peso ha sido fallida"
        $ vidas = vidas - 1
    else:
        l "Muy bien, el objetivo principal de la cobertura cambiaria es brindar certidumbre financiera para hacer frente a los compromisos en moneda extranjera."
        l "Gracias a esto la revaluación no tuvo mayor impacto en la empresa."
        $ crisis1_sol = True
    jump iniciar_caso1

label crisis_2:
    if(opcion == 0):
        l "%(username)s hace unos dias se presentaron unos fuertes vientos destruyendo la mitad del total del area cultivada de la empresa..."
        l "...el fenomeno natural causo destrozos en las plantas al caer sobre ellas postes cables y plásticos, con la consiguiente pérdida de la producción actual y hacia futuro."
        l "Toma la mejor decisión para superar esta crisis"
        menu:
            "Reducir personal":
                jump reducir_personal
            "Prestamo de FINAGRO":
                jump prestamo
            "Generar valor agregado":
                jump generar_valor
    if opcion != 6:
        l "Lo siento, la decisión tomada para hacer frente a la pérdida de infraestructura no tuvieron los efectos deseados"
        $ vidas = vidas - 1
    else:
        l "Muy bien, el prestamo contribuyo a recuperar gran parte de la infraestructura y a aumentar la producción"
        l "El fenomeno natural fue afrontado satisfactoriamente"
        $ crisis2_sol = True
    jump iniciar_caso1
    
label ampliacion_portafolio:
    l "Mediante la estrategia de diversificacion concentrica se produciran mas variedades de flores lo cual atendera las necesidades de varios segmentos del mercado a nivel mundial."
    l "Deseas tomar esta opción?"
    menu:
        "Si":
            $ opcion = 1
        "No":
            user "Me podrias repetir las opciones"
    if cual_crisis == 1:
        jump crisis_1
    elif cual_crisis == 2:
        jump crisis_2
    elif cual_crisis == 3:
        jump crisis_3
    elif cual_crisis == 4:
        jump crisis_4

label provecho_estaciones:
    l "Colombia por no poseer estaciones, tiene las condiciones de medio ambiente propicias para que el proceso de producción de flores no sufra desaceleraciones y se mantenga constante."
    l "Si toma esta opcion se incrementara la producción en épocas donde la competencia internacional no pueda producir al mismo nivel nuestro a causa de las estaciones."
    l "Desea hacer esto?"
    menu:
        "Si":
            $ opcion = 2
        "No":
            user "Me podrias repetir las opciones"
    if cual_crisis == 1:
        jump crisis_1
    elif cual_crisis == 2:
        jump crisis_2
    elif cual_crisis == 3:
        jump crisis_3
    elif cual_crisis == 4:
        jump crisis_4

label cobertura_cambiaria:
    l "A traves de la cobertura cambiaria es posible fijar el tipo de cambio en el presente para realizar operaciones futuras de divisas a cambio de una prima."
    l "Quiere hacer esto?"
    menu:
        "Si":
            $ opcion = 3
        "No":
            user "Me podrias repetir las opciones"
    if cual_crisis == 1:
        jump crisis_1
    elif cual_crisis == 2:
        jump crisis_2
    elif cual_crisis == 3:
        jump crisis_3
    elif cual_crisis == 4:
        jump crisis_4

label reducir_personal:
    l "Se despedira gran parte de los empleados vinculados a la empresa esto con el fin de reducir costos."
    l "Deseas hacer esto?"
    menu:
        "Si":
            $ opcion = 4
        "No":
            user "Me podrias repetir las opciones"
    if cual_crisis == 1:
        jump crisis_1
    elif cual_crisis == 2:
        jump crisis_2
    elif cual_crisis == 3:
        jump crisis_3
    elif cual_crisis == 4:
        jump crisis_4
label generar_valor:
    l "Haras que el producto sea diferenciado con respecto a la competencia y generaras condiciones para pensar en un incremento de precio en el producto"
    l "Quieres hacer esto?"
    menu:
        "Si":
            $ opcion = 5
        "No":
            user "Me podrias repetir las opciones"
    if cual_crisis == 1:
        jump crisis_1
    elif cual_crisis == 2:
        jump crisis_2
    elif cual_crisis == 3:
        jump crisis_3
    elif cual_crisis == 4:
        jump crisis_4
label prestamo:
    l "Este prestamo financiado por FINAGRO debe utilizarse para invertir en infraestructura y en cultivos."
    l "Deseas pedir este prestamo?"
    menu:
        "Si":
            $ opcion = 6
        "No":
            user "Me podrias repetir las opciones"
    if cual_crisis == 1:
        jump crisis_1
    elif cual_crisis == 2:
        jump crisis_2
    elif cual_crisis == 3:
        jump crisis_3
    elif cual_crisis == 4:
        jump crisis_4