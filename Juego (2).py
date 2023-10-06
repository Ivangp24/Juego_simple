#!/usr/bin/env python
# coding: utf-8

# # Juego

# In[1]:


import time
import random



def introduccion():
    print("Estás en medio de una nave espacial abandonada, flotando en el vacío del espacio profundo.")
    time.sleep(2)
    print("Sientes una opresiva oscuridad y un escalofrío recorre tu espalda.")
    time.sleep(2)
    print("De repente, te encuentras solo en un cruce de pasillos oscuros.")
    time.sleep(2)
    print("Tienes que tomar una decisión. ¿Qué harás?")


    
def eleccion_camino():
    eleccion = input("¿Tomarás el 'Pasillo Izquierdo' o el 'Pasillo Derecho'? ").lower()
    if eleccion == "pasillo izquierdo":
        print("Decidiste tomar el Pasillo Izquierdo.")
        time.sleep(2)
        pasillo_izquierdo()
    elif eleccion == "pasillo derecho":
        print("Decidiste tomar el Pasillo Derecho.")
        time.sleep(2)
        pasillo_derecho()
    else:
        print("Esa no es una elección válida. Intenta de nuevo.")
        eleccion_camino()


        
def pasillo_izquierdo():
    print("Mientras avanzas por el Pasillo Izquierdo, escuchas pasos sigilosos acercándose.")
    time.sleep(2)
    print("De repente, Predator, la criatura alienígena cazadora, aparece frente a ti.")
    time.sleep(2)
    print("Predator te observa y toma una decisión. Puede ayudarte o considerarte una amenaza.")
    time.sleep(2)
    eleccion = input("Escribe 'ayuda' para tratar de pedir ayuda a Predator o 'huir' para escapar: ").lower()
    if eleccion == "ayuda":
        print("Predator decide ayudarte y te muestra una salida segura.")
        time.sleep(2)
        print("Se despide de ti, pero antes te dice que está en busca de una cripta.")
        time.sleep(2)
        print("Te da un papel en el que viene escrito la palabra teclado y se va. No entiendes nada. sigues adelante.")
        time.sleep(2)
        pasillo_izquierdo_continuacion()
    elif eleccion == "huir":
        print("Intentas huir, pero Predator interpreta tu movimiento como una amenaza.")
        time.sleep(2)
        print("Predator te lanza su lanza y te la clava en la espalda, atravesando tu corazón.")
    else:
        print("Esa no es una elección válida. Predator no entiende tus intenciones. Intenta de nuevo.")
        time.sleep(2)
        pasillo_izquierdo()
        

        
def pasillo_izquierdo_continuacion():
    print("Avanzas por el pasillo y llegas a una habitación extraña.")
    time.sleep(2)
    print("En el centro de la habitación, ves a un cienpiés alienígena gigante.")
    time.sleep(2)
    print("El cienpiés parece agitado y peligroso.")
    time.sleep(2)

    tu_vida = random.randint(80, 100)
    cienpies_vida = random.randint(100, 150)

    print(f"Tu vida: {tu_vida}")
    print(f"Vida del cienpiés: {cienpies_vida}")

    while tu_vida > 0 and cienpies_vida > 0:
        print("\nEs tu turno. Elige un ataque:")
        print("1. Tirar piedra")
        print("2. Disparo láser")
        print("3. Llamarada")

        tu_turno = input("Selecciona una opción (1/2/3): ")

        if tu_turno == '1':
            ataque_tu = random.randint(10, 20)
            print(f"Le tiras una piedra del suelo y le infliges {ataque_tu} de daño.")
            cienpies_vida -= ataque_tu
        elif tu_turno == '2':
            ataque_tu = random.randint(15, 30)
            print(f"Utilizas tu pistola láser y le infliges {ataque_tu} de daño.")
            cienpies_vida -= ataque_tu
        elif tu_turno == '3':
            ataque_tu = random.randint(20, 40)
            print(f"Utilizas tu lanzallamas y le infliges {ataque_tu} de daño.")
            cienpies_vida -= ataque_tu
        else:
            print("Selección no válida. Pierdes tu turno.")

        if cienpies_vida <= 0:
            print("Has derrotado al cienpiés alienígena.")
            time.sleep(2)
            print("Encuentras un portal al fondo de la habitación y decides adentrarte...")
            time.sleep(2)
            portal_misterioso()
            break

        ataque_cienpies = random.randint(10, 30)
        print(f"\nEs el turno del cienpiés. Te ataca y te inflige {ataque_cienpies} de daño.")
        tu_vida -= ataque_cienpies

        if tu_vida <= 0:
            print("El cienpiés alienígena te derrotó y te arranca la cabeza de un mordisco.")
            break

        print(f"Tienes: {tu_vida} de vida. ")
        print(f"Al cienpiés le quedan: {cienpies_vida} de vida.")



    
def portal_misterioso():
    print("Al entrar pierdes la visión durante unos segundos por la irradiante luz blanca del lugar.")
    time.sleep(2)
    print("Recuperas la vista, alzas la cabeza y te das cuenta de que estás en...")
    time.sleep(2)
    print("El cielo? Es un lugar completamente vacío, solo te encuentras tú ante la inmensidad de la nada.")
    time.sleep(2)
    print("Te fijas que ante tus pies hay una GameBoy. La coges y empiezas a jugar, sin saber muy bien por qué.")
    time.sleep(2)
    print("\nEl juego comienza. Cuidado esto podría tener graves consecuencias. Adivina el número.")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while intentos < 6:
        intentos += 1
        try:
            adivinanza = int(input(f"Intento {intentos}: Adivina el número secreto (entre 1 y 100): "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if adivinanza == numero_secreto:
            print(f"Has adivinado el número secreto ({numero_secreto}). Has ganado el juego.")
            time.sleep(1)
            print("El lugar en el que estás empieza a agitarse y pierdes la consciencia.")
            time.sleep(1)
            print("Despiertas en tu cama, en tu casa. Te llega una notificación al móvil.")
            time.sleep(1)
            print(f"Es una notificación del banco. El número secreto del videojuego ({numero_secreto}) se ha multiplicado por un millón y ese es el saldo en tu cuenta, ganaste.")
            break
        elif adivinanza < numero_secreto:
            print("El número secreto es mayor. Sigue intentando.")
        else:
            print("El número secreto es menor. Sigue intentando.")

    else:
        print(f"Has agotado tus 5 intentos. El número secreto era {numero_secreto}.")
        time.sleep(1)
        print("El videojuego te absorve. Vivirás por siempre en él, hasta que alguien vuelva a jugar al juego y pierda. Suerte.")



def pasillo_derecho():
    print("Avanzas por el Pasillo Derecho y llegas a una puerta que te teletransportará a un lugar secreto.")
    time.sleep(2)
    print("Abres la puerta, entras y apareces en una cripta oscura y misteriosa.")
    time.sleep(2)
    print("En el centro de la cripta, encuentras a un ente místico y poderoso de un planeta lejano.")
    time.sleep(2)
    print("El ente te mira fijamente y te plantea una adivinanza.")
    time.sleep(2)
    print("Tienes que responder correctamente para continuar tu viaje.")
    adivinanza = "Tengo llaves, pero no tengo cerraduras. Tengo un espacio, pero no una habitación. Puedes entrar, pero no puedes salir. ¿Qué soy yo?"
    respuesta_correcta = "teclado"
    respuesta = input(f"Adivinanza: {adivinanza}\nTu respuesta: ").lower()
    if respuesta == respuesta_correcta:
        print("Has respondido correctamente. El ente místico sonríe y te concede una ofrenda.")
        time.sleep(2)
        print("Despiertas, te sientes cansado. Eso pareció muy real...")
        time.sleep(2)
        print("Al cabo de un tiempo te das cuenta de que no envejeces. Eres inmune a cualquier enfermedad o ataque. Eres inmortal...")
    else:
        print("Tu respuesta es incorrecta. El ente místico desaparece y quedas atrapado para el resto de tus días en el interior de la cripta.")
        time.sleep(2)
        print("O quizás...")
        time.sleep(2)
        ayuda_misteriosa()
        


def ayuda_misteriosa():
    print("Escuchas sonidos en una de las paredes de la cripta.")
    time.sleep(2)
    print("Alguien te está hablando y te dice:")
    time.sleep(2)
    print("Somos el equipo de investigación de la nave. En frente de nosotros tenemos una palanca.")
    time.sleep(2)
    print("Dependiendo de tu suerte tiraremos de ella o no. No queremos hacernos responsables de que sea algo malo o bueno.")
    time.sleep(2)
    print("Hemos tirado una moneda. Adivina, cara o cruz. Tienes 2 intentos.")
    
    resultados_posibles = ["cara", "cruz"]
    intentos = 0

    while intentos < 2:
        moneda = random.choice(resultados_posibles)
        adivinanza = input("\nIntento " + str(intentos + 1) + ": ¿Cara o cruz? ").lower()

        if adivinanza == moneda:
            print("Has acertado, la moneda cayó de " + moneda + ". Tiraremos de la palanca. Buena suerte.")
            time.sleep(2)
            print("Se abre un portal frente a ti. Decides andentrarte en él.")
            time.sleep(2)
            portal_misterioso()
        else:
            print("Lo siento, la moneda cayó " + moneda + ".")

        intentos += 1

    else:
        print("Mala suerte, el destino habló.")
        time.sleep(2)
        print("Tus restos premanecieron por siempre en la cripta. DEP.")
        
        





introduccion()
eleccion_camino()


# In[ ]:




