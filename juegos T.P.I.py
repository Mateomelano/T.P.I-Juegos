menu = 0
while menu == 0:
    print("SELECCIONE CON UN NUMERO CUAL DESEA JUGAR")
    menu = int((input("1 TA-TE-TE. 2  Quiz Preguntas. 3 Piedra Papel o Tijera. 4 Adivinanza , 5 Para salir del sistema \n")))
    if menu == 1:
                tablero = [ "-", "-", "-",  # Tablero del juego
                            "-", "-", "-",
                            "-", "-", "-",]
                ganador = None  # variable global desactivada

                def mostrartablero():  # Funcion que muestra el tablero y sus posiciones
                    print("\n")
                    print(tablero[0] + "|" + tablero[1] +
                        "|" + tablero[2]+"           1|2|3")
                    print(tablero[3] + "|" + tablero[4] +
                        "|" + tablero[5]+"           4|5|6")
                    print(tablero[6] + "|" + tablero[7] +
                        "|" + tablero[8]+"           7|8|9")
                    print("\n")

                def juego():
                    i = 0  # Valor contadorD
                    x = 0
                    global ganador
                    print("¡¡Bienvenido al Juego del TA-TE-TI!!")
                    while i < 9:  # Mientras el contador intentos sea menor a 9
                        for x in range(1):  # Intento del jugador 1 (O)
                            print("Le toca al jugador 1 = O")
                            valor = "O"
                            mostrartablero()  # Muestra el tablero
                            turnos(valor)  # Se le da valor a la funcion turnos
                            controlganador()  # Se controla si gano
                            i = i+1  # Se suma 1 valor a i
                            if ganador != "O":  # Condicion si gana el jugador 1
                                if i < 9:  # Mientras el contador intentos sea menor a 9
                                    for j in range(1):  # Intento del jugador 2 (X)
                                        print("Le toca al jugador 2 = X")
                                        mostrartablero()
                                        valor = "X"
                                        turnos(valor)
                                        controlganador()
                                        i = i+1
                                        global menu
                                        if ganador == "X":  # Condicion si gana el jugador 2
                                            print("---------- GANO JUGADOR 2 ----------")
                                            i = 10
                                            menu = int(0)
                            else:
                                print("---------- GANO JUGADOR 1 -----------")
                                i = 10
                                menu = int(0)
                    if i == 9:
                        print("--------------EMPATE------------------")
                        menu = int(0)

                def turnos(valor):
                    check = False  # Check esta apagada
                    while check == False:#While1
                        posc = (input("\nElegi una posicion de 1 - 9\n"))
                        if not posc.isnumeric(): #C1. Funcion para verificar que sea una letra y no un numero o caracter
                            print("Usted eligio un caracter no valido, ingrese un numero.")
                        else:#Else1  
                            posc = int(posc)#Se pasa a int para poder ejecutar la linea de abajo
                            posc = (posc - 1)# porque en la lista se empieza desde cero
                            if posc >= 0 and posc <= 9:  #C2 Se verifica que el numero sea entre 0 y 9
                                if tablero[posc] == "-":  #C3 Se verifica que la posicion este desocupada
                                    check = True
                                else:#Else2
                                    print("Esa posicion ya esta ocupada")
                            else:#Else3
                                print("El numero que ingreso es mayor a 9, ingrese uno valido")
                    tablero[posc] = valor
                    mostrartablero()

                def controlganador():  # Funcion que contiene todas las funciones que verifican a los jugadores
                    global ganador  # Variable global que se activa si alguna de las funciones de verificacion se ejecuta
                    controllinea()  # Funcion para el control en linea
                    controlver()  # Funcion para el control en vertical
                    controldiag()  # Funcion para el control en diagonal

                def controllinea():
                    global ganador
                    if tablero[0] == tablero[1] == tablero[2] != "-":
                        # Ganador toma el valor de de la posicion del simbolo que representa al ganador
                        ganador = tablero[1]
                    elif tablero[3] == tablero[4] == tablero[5] != "-":
                        ganador = tablero[3]
                    elif tablero[6] == tablero[7] == tablero[8] != "-":
                        ganador = tablero[6]

                def controlver():
                    global ganador
                    if tablero[0] == tablero[3] == tablero[6] != "-":
                        ganador = tablero[0]
                    elif tablero[1] == tablero[4] == tablero[7] != "-":
                        ganador = tablero[1]
                    elif tablero[2] == tablero[5] == tablero[8] != "-":
                        ganador = tablero[2]

                def controldiag():
                    global ganador
                    if tablero[0] == tablero[4] == tablero[8] != "-":
                        ganador = tablero[0]
                    elif tablero[2] == tablero[4] == tablero[6] != "-":
                        ganador = tablero[2]

                juego()  # Se ejecuta la funcion del juego
    elif menu == 2:
                print("!!Bienvenido al juego de las preguntas¡¡")
                tot = 0 # Acumulador de puntos
                i = 1 # Contador While
                while i > 0: #WHILE1 .Si el contador vale 1:
                    print("LA PRIMER PREGUNTA ES \nQuien gano la copa del mundo en 1986?") # Pregunta.
                    print("---------------------------------\n1. Argentina . 2 Portugal . 3. Brasil . 4 Alemania.  ") # Opciones a elegir.
                    puntos1= input("Escribe 1,2,3 o 4\n") # El jugador imprime su respuesta.
                    while not puntos1.isnumeric():#while2
                         puntos1 = input("Digite una respuesta valida, no se permiten caracteres\n")
                    puntos1 = int(puntos1) 
                    while puntos1 > 4:#while3
                        puntos1 = int(input("Digite un numero entre 1 y 4\n"))                   
                    if puntos1 == 1: #C1. Se verifica si la respuesta es correcta y se suman lo puntos si asi lo es.
                        tot = (tot + 20)
                    print("LA SEGUNDA PREGUNTA ES\nQuien es el arquero titular de la seleccion Argentina ")
                    print("---------------------------------\n1. Dibu Martinez .2 Franco Armani. 3 Martin Guzman. 4 Geronimo Rulli")
                    puntos2 = input("Escriba 1,2,3,4\n")
                    while not puntos2.isnumeric():
                         puntos2 = input("Digite una respuesta valida, no se permiten caracteres\n")
                    puntos2 = int(puntos2) 
                    while puntos2 > 4:
                        puntos2 = int(input("Digite un numero entre 1 y 4\n")) 
                    if puntos2==1:
                        tot = (tot + 20)          
                    print("LA TERCER PREGUNTA ES\n¿Quién es el capitán de la selección argentina?")
                    print("-------------------------------------\n1. Rodrigo de Paul. 2 Lautaro Martinez . 3 Nicolas Otamendi. 4 Leonel Messi")
                    puntos3 = input("Escriba 1,2,3 O 4\n")
                    while not puntos3.isnumeric():
                         puntos3 = input("Digite una respuesta valida, no se permiten caracteres\n")
                    puntos3 = int(puntos3) 
                    while puntos3 > 4:
                        puntos3 = int(input("Digite un numero entre 1 y 4\n")) 
                    if puntos3== 4:
                        tot = (tot + 20)
                    print("LA CUERTA PREGUNTA ES\n¿Con cuales de estas selecciones argentina disputa la fase de grupos de Qatar 2022?")
                    print("-------------------------------------\n1. Paises Bajos. 2 Qatar .3 Mexico. 4 Senegal.")
                    puntos4 = input("Escriba 1,2,3 O 4\n")
                    while not puntos4.isnumeric():
                         puntos4 = input("Digite una respuesta valida, no se permiten caracteres\n")
                    puntos4 = int(puntos4) 
                    while puntos4 > 4:
                        puntos4 = int(input("Digite un numero entre 1 y 4\n")) 
                    if puntos4==3:
                        tot = (tot + 20)
                    print("LA QUINTA PREGUNTA ES\n¿Contra que equipo Argentina disputo su ultima final?")
                    print("-------------------------------------\n1. España. 2 Brasil. 3 Chile. 4 Italia")
                    puntos5 = input("Escriba 1,2,3 O 4\n")
                    while not puntos5.isnumeric():
                         puntos5 = input("Digite una respuesta valida, no se permiten caracteres\n")
                    puntos5 = int(puntos5) 
                    while puntos5 > 4:
                        puntos5 = int(input("Digite un numero entre 1 y 4\n")) 
                    if puntos5==4:
                        tot = (tot + 20)
                    rtatotal = (puntos1,puntos2,puntos3,puntos4,puntos5) # Se agrupan las respuestas del jugador
                    print ("Los puntos finales son ", tot , "De 100") # Se declara la puntuacion del jugador
                    print("Sus respuestas fueron", rtatotal) # Se imprimen las respuestas del jugador
                    print("Las respuestas correctas eran\n1: 1\n2: 1\n3: 4\n4: 3\n5: 4  ") # Se imprimen las respuestas correctas
                    menu = int(0)
                    break
    elif menu == 3:
                import random # funcion random 
                print("!!BIEVENIDO AL PIEDRA PAPEL TIJERA!!")
                jugador = input("Elija piedra, papel o tijera, recuerde que esta jugando contra el sistema\n") #El jugador ingresa su opcion
                jugador = jugador.upper() #Se utiliza la funcion .upper(), para la opcion sea pasada a mayusculas
                opciones = ["PIEDRA", "PAPEL", "TIJERA"] #Opciones que puede elegir el jugador
                while jugador not in opciones:  #WHILE1 Mientras el jugador no elija piedra, papel o tijera. #WHILE1
                    jugador = input("Ingreso una opcion no valida, elija piedra, papel o tijera \n")
                    jugador = jugador.upper() #Se utiliza la funcion .upper(), para la opcion sea pasada a mayusculas
                computadora = random.choice(opciones) #La computadora genera la opcion random
                computadora = computadora.upper()
                if jugador == computadora: #C1. Condicion de empate
                    print("La compu eligio", computadora)
                    print("Jugador eligio", jugador)
                    print("EMPATARON!!")
                    menu = int(0)
                elif jugador == "PIEDRA": #ELIF1. Condicion si el jugador elige "piedra"
                    if computadora == "PAPEL": #C2
                        print("La compu eligio", computadora)
                        print("Jugador eligio", jugador)
                        print("!!Perdiste!!")
                        menu = int(0)
                    if computadora == "TIJERA": #C3
                        print("La compu eligio", computadora)
                        print("Jugador eligio", jugador)
                        print("!!Ganaste!!")
                        menu = int(0)
                elif jugador == "PAPEL": #ELIF2. Condicion si el jugador elige "papel"
                        if computadora == "TIJERA":#C4
                            print("La compu eligio", computadora)
                            print("Jugador eligio", jugador)
                            print("!!Perdiste!!")
                            menu = int(0)
                        if computadora == "PIEDRA":#C5
                            print("La compu eligio", computadora)
                            print("Jugador eligio", jugador)
                            print("!!Ganaste!!")
                            menu = int(0)
                elif jugador == "TIJERA": #ELIF3. Condicion si jugador elige tijera
                        if computadora == "PIEDRA":#C6
                            print("La compu eligio", computadora)
                            print("Jugador eligio", jugador)
                            print("!!Perdiste!!")
                            menu = int(0)
                        if computadora == "PAPEL":#C7
                            print("La compu eligio", computadora)
                            print("Jugador eligio", jugador)
                            print("!!Ganaste!!")
                            menu = int(0)
    elif menu == 4:
                from random import randint # Libreria para generar numero random
                intentos = 0 # Contador Intentos
                print("!!BIENVENIDO AL JUEGO DE ADIVINAR UN NUMERO¡¡")
                num = (input("Digite el numero que cree que sera, recuerde que es del 1 al 100 y si digita un numero mayor a 100 se le descontara un intento.\n"))
                while not num.isnumeric(): #While1 Funcion para verificar que el numero no sea una letra
                    num = (input("Ingrese un numero por favor \n"))
                if num.isnumeric():#C1
                    num = int(num)
                    num2 = int(randint(0, 100)) # Se genera el numero random de (0,100)
                    print("El numero que digito es", num)
                    print("Recuerde, tiene 5 intentos para adivinar el numero")
                    while intentos < 5:#While2
                        if num == num2: #C2 Condicion si gana
                            print("¡¡Felicitaciones, Adivinaste el numero!!")
                            intentos = 6
                            menu = int(0)
                        elif num != num2:#Elif1
                            if num < num2: # C3. Condicion si el numero que digito el jugador es menor al numero randon 
                                num = (input("El numero que tiene que adivinar es mayor, Porfavor intente nuevamente \n"))
                                while not num.isnumeric(): #While3 (Funcion que se ejecuta si el usuario pone una letra)
                                    num = (input("Ingrese un numero por favor\n"))
                                num = int(num)
                                intentos = (intentos + 1)
                            else: #Else1. Si la primera condicion no se cumple se ejecuta esta (el numero que digito el jugador es mayor al numero random)
                                num = (input("El numero que tiene que adivinar es menor, Porfavor intente nuevamente \n"))
                                while not num.isnumeric():#While4 (Funcion que se ejecuta si el usuario pone una letra)
                                    num = (input("Ingrese un numero por favor\n"))
                                num = int(num)
                                intentos = (intentos + 1)
                            if intentos == 5: #C4 .Si el jugador llega a los 5 intentos, verifica si gano en el ultimo o si perdio.
                                if num == num2:#C5
                                    print("!!Felicitaciones adivinaste el numero¡¡")
                                    menu = int(0)
                                else:#Else2
                                    print("¡!Te quedaste sin intentos¡!")
                                    print("El numero era", num2)
                                    menu = int(0)
    elif menu == 5:
            print ("!!Gracias por jugar!!")
            break