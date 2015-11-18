#begin characters
define l = Character(_("Esperanza"), color="#ffcccc")


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


        
label fight_1(php=3):
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
    if crisis1_sol is True and crisis2_sol is True and crisis3_sol is True and crisis4_sol is True:
        l "Felicidades la empresa ha atrevasado todas estas crisis gracias a tus acertadas decisiones"
        return
    call fight_1(vidas)# from _call_fight_1
    if vidas == 0:
        l "Has perdido"
        return
    
    user "Que hay pendiente por hacer?"
    
    #window hide None
    #call screen caso_1_imagemap
    #window show None
    call fight_1(vidas)
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
        "Crisis de mercado y guerra de precios":
            if crisis3_sol is False:
                $ cual_crisis = 3
                jump crisis_3
            else:
                l "No te preocupes, este problema ya lo has solucionado."
                jump iniciar_caso1
        "Demando por Dumping":
            if crisis4_sol is False:
                $ cual_crisis = 4
                jump crisis_4
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
    
label crisis_3:
    if(opcion == 0):
        l "%(username)s la empresa esta siendo afectada por una guerra de precios debido a que el sector floricultor en Colombia está creciendo de manera acelerada..."
        l "La situación es que se está presentando una sobre oferta en el mercado, una saturación de flores para y para poder competir en el mercado internacional habria que bajar los precios."
        l "Toma la mejor decisión para superar esta crisis"
        menu:
            "Ampliacion del portafolio de productos":
                jump ampliacion_portafolio
            "Aumentar la productividad y reducir costos":
                jump aumentar_productividad
            "Generar valor agregado":
                jump generar_valor
    if opcion != 5:
        l "Lo lamento, la estrategia llevada a cabo para solucionar esta crisis fue fallida. Los propietarios estan muy "
        $ vidas = vidas - 1
    else:
        l "Muy bien, la empresa salio bien librada de esto sin sacrificar costos"
        $ crisis3_sol = True
    jump iniciar_caso1
    
label crisis_4:
    if(opcion == 0):
        l "%(username)s nuestra empresa esta ganando terreno en Estados Unidos, pero al mismo tiempo los productores locales de California y Florida..."
        l "... Una asociación de floricultores norteamericanos han demandado nuestra empresa por dumping. "
        l "Necesitamos tomar una decisión lo más pronto posible."
        menu:
            "Proceso Jurídico":
                jump proceso_juridico
            "Generar valor agregado":
                jump generar_valor            
    if opcion != 8:
        l "Lo siento, la decision que has tomado no ha sido satisfactoria y la demanda sigue en pie"
        $ vidas = vidas - 1
    else:
        l "Muy bien, la demanda ha sido afrontada correctamente y se llego a un acuerdo con los comerciantes locales"
        $ crisis4_sol = True
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
label aumentar_productividad:
    l "Por medio de esta estrategia elevaras la producción de la empresa a costas de las utilidades actuales de la empresa reduciendo los costos"
    l "Quieres hacer esto?"
    menu:
        "Si":
            $ opcion = 7
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
label proceso_juridico:
    l "Contrataras a un grupo de abogados para que atiendan este caso, esto conlleva un gasto imprevisto para la empresa"
    l "Quieres hacer esto?"
    menu:
        "Si":
            $ opcion = 8
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