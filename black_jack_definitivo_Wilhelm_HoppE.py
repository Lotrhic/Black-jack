import random

espadas =  ["A♠","1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠","1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠","1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
corazones =["A♠","1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠","1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠","1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
diamantes =["A♦","1♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦","1♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦","1♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"]
treboles = ["A♣","1♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣","1♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣","1♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"]

baraja = []
baraja = espadas + corazones + diamantes + treboles

maquina      = 0  #sumatoria de valores de las cartas de la maquina
jugador      = 0  #sumatoria de valores de las cartas del jugador
cartajugador = 0  
cartamaquina = 0

def limpiarPantalla():
    """subrutina que imprime lineas en blanco
    para limpear la pantalla
    Entradas: ninguna
    Salidas: 40 lineas en blanco
    """
    print("\n"*40)

def sacarCarta():
    if baraja!=[]:
        carta = random.choice(baraja)
        print(carta)
        baraja.remove(carta)
        return carta
    else:
        print("Ya no hay cartas en la baraja")


def sacarSegundaCarta():
    if baraja!=[]:
        carta = random.choice(baraja)
        baraja.remove(carta)
        return carta
    else:
        print("Ya no hay cartas en la baraja")

def sinCartas():
    if baraja==[]:
        print("Ya no hay cartas en el mazo")
        return False
    else:
        return True
def valorCarta(c):
    v = 0  #va a contener el valor correspondiente de la carta extraida
    if baraja!=[]:
        if c[0] == "2":
            v = 2
        elif c[0] == "3":
            v = 3
        elif c[0] == "4":
            v = 4
        elif c[0] == "5":
            v = 5
        elif c[0] == "6":
            v = 6
        elif c[0] == "7":
            v = 7
        elif c[0] == "8":
            v = 8
        elif c[0] == "9":
            v = 9
        elif c[0] == "1":
            v = 10
        elif c[0] in "JQK":
            v = 10
        elif c[0] == "A":
            v = 11
        return v
    else:
        print("No hay más carta en el mazo.")

def game():
    op = 0
    while(True):
        menu()
        op = input("Digite la opción: ")
        while op not in "123":
            print("Solo pueden ser numero entre 1 y 3")
            break

        else:
            op=int(op)
            if op == 1:
                print("Inicio de la partida")
                juego21()
            elif op == 2:
                print("")
                print("")
                print("")
                print("Una vez que cada participante tenga las dos cartas se puede presentar los siguientes casos: ")
                print("")
                print("    1. Que ambos participantes tengan 21 puntos exactos. En este caso automáticamente la casa resultará ganadora. Además todo empate en puntos, la casa gana.")
                print("")
                print("    2. Que uno de los participantes tenga 21 puntos. Si el participante que tiene 21 es la casa, automáticamente ganaria el juego. ""\n""En caso contrario el juego seguiría vivo con las reglas que se describen más adelante.")
                print("")
                print("    3. Si ambos participantes tienen menos que 21 puntos, se debe en este caso aplicar las nuevas reglas del juego.")
                print("")
                print("Cuando se esté en la situación del punto 3, es porque la sumatoria de puntos es menor que 21 para ambos casos, siendo necesario primero que el jugador tome algunas de las siguientes decisiones: ")
                print("")
                print("    a. Si tiene de 16 a 20 puntos podria QUEDARSE, es decir que no va a solicitar ninguna carta más, siendo esto algo NO es obligatorio.")
                print("")
                print("    b. Estando en la situación del punto a o menor, podria PEDIR una o más cartas con la intención de acercarse lo más posible al objetivo de 21 puntos y tomar la decisión de QUEDARSE.")
                print("")
                print("    c. Podría suceder que al solicitar más cartas, el jugador exceda los 21 puntos, entonces habrá perdido automáticamente la partida con la casa.")
                print("")
                print("Si el jugador se queda o tiene exactamente 21 puntos, llega el turno de la máquina. Pudiéndose dar los siguientes pasos: ")
                print("")
                print("    d. Si el jugador tiene exactamente 21 puntos y la casa MENOS de 17 puntos, entonces a la casa se le reparte una nueva carta, esto se hará  hasta que suceda alguno de los siguientes casos: ")
                print("")
                print("        A. Si la suma de puntos de la casa es 21, por regla la casa gana la partida.")
                print("")
                print("        B. Si la suma de puntos de la casa es menor que 21 pero mayor que la suma de puntos del jugador, entonces la casa gana la partida. En  caso de empate de puntos, la casa gana.")
                print("")
                print("        C. Si la suma de puntos del jugador es mayor que el de la casa, entonces el jugador gana la partida.")
                print("")
                print("        D. Si la suma de puntos de la casa es mayor de 21, el jugador gana la partida.")
                print("")
                print("                                                         IMPORTANTE")
                print("La casa está obligada a tomar cartas adicionales cuando su puntaje sea menor o igual a 16, si tiene 17 o más se debe quedar.")
                print("")
                print("")
                print("")

            elif op == 3:
                print("Fin del juego")
                break

    
def menu(): #esto es un procedimiento
    print("╔═══════════════════╗")
    print("║ 1. Jugar          ║")
    print("║ 2. Reglas         ║")
    print("║ 3. Salir          ║")
    print("╚═══════════════════╝")

def juego21(): #programa principal

    while True:
    
        ganador      = False 
        sumaCasa  = 0     #sumatoria de valores de las cartas de la maquina
        sumaJugador  = 0     #sumatoria de valores de las cartas del jugador
        cartaJugador = ""    #contiene el valor de la carta del jugador
        cartaCasa = ""    #contiene el valor de la carta de la maquina
        masCartasJ   = True  #controla si el usuario ya no quiere más cartas
        otraCarta    = ""

        #inicia el juego
        limpiarPantalla()
        sinCartas()

        #repartiendo la primera carta
        print("Repartiendo carta a la casa")
        cartaCasa = sacarCarta() #saca una carta de la baraja, es un string
        print(cartaCasa)         #muestra la carta correspondiente
        print(valorCarta(cartaCasa))
        sumaCasa = sumaCasa + valorCarta(cartaCasa)
        print("Sumatoria de la Casa: ", sumaCasa)
        
        sinCartas()
        print("Repartiendo carta al jugador")
        cartaJugador = sacarCarta()
        print(cartaJugador)
        print(valorCarta(cartaJugador))
        sumaJugador = sumaJugador + valorCarta(cartaJugador)
        print("Sumatoria del Jugador: ", sumaJugador)
        
        #repartiendo la segunda carta
        sinCartas()   
        cartaCasa = sacarSegundaCarta() #saca una carta de la baraja, es un string
        sumaCasa = sumaCasa + valorCarta(cartaCasa)
        print("La casa se repartio una nueva carta")

        sinCartas()    
        print("Repartiendo carta al jugador")
        cartaJugador = sacarCarta()
        print(cartaJugador)
        print(valorCarta(cartaJugador))
        sumaJugador = sumaJugador + valorCarta(cartaJugador)
        print("Sumatoria del Jugador: ", sumaJugador)
        
        ######################### JUGADOR #########################  

        #preguntar al jugador si quiere más cartas

        while sumaCasa<=16:
            cartaCasa = sacarSegundaCarta() #saca una carta de la baraja, es un string           
            sumaCasa = sumaCasa + valorCarta(cartaCasa)         
            print("La casa se repartio una nueva carta")
            if sumaCasa > 16:
                break
        

        si="Y"
        no="N"
        while masCartasJ != False:
            sinCartas()
            otraCarta = input("Desea una carta más: (Y)/(N)")
            if otraCarta == si.lower():
                print("Repartiendo carta al jugador")
                cartaJugador = sacarCarta()
                print(cartaJugador)
                print(valorCarta(cartaJugador))
                sumaJugador = sumaJugador + valorCarta(cartaJugador)
                print("Sumatoria nueva del Jugador: ", sumaJugador)
                
                if sumaJugador > 21:
                    print("La casa tiene "+str(sumaCasa)+" y el jugador tiene "+str(sumaJugador)+" el jugador")
                    print("")
                    print(" _____ _              _      ")
                    print("|  __ (_)            | |     ")
                    print("| |__) |  ___ _ __ __| | ___ ")
                    print("|  ___/ |/ _ \ '__/ _` |/ _ \ ")
                    print("| |   | |  __/ | | (_| |  __/")
                    print("|_|   |_|\___|_|  \__,_|\___|")
                    print("")
                    print("")
                    break
                elif sumaJugador == 21 and sumaCasa == 21:
                    print("La casa y el jugador tienen "+str(sumaCasa)+" el jugador.")
                    print("")
                    print(" _____ _              _      ")
                    print("|  __ (_)            | |     ")
                    print("| |__) |  ___ _ __ __| | ___ ")
                    print("|  ___/ |/ _ \ '__/ _` |/ _ \ ")
                    print("| |   | |  __/ | | (_| |  __/")
                    print("|_|   |_|\___|_|  \__,_|\___|")
                    print("")
                    print("")
                    break
            elif otraCarta==no.lower():
                masCartasJ = False

#jugador pierda
                if sumaCasa<=21:

                    if sumaCasa==sumaJugador or sumaJugador>21 or sumaCasa>sumaJugador:
                        print("La casa tiene "+str(sumaCasa)+" el jugador tiene "+str(sumaJugador)+" el jugador")
                        print("")
                        print(" _____ _              _      ")
                        print("|  __ (_)            | |     ")
                        print("| |__) |  ___ _ __ __| | ___ ")
                        print("|  ___/ |/ _ \ '__/ _` |/ _ \ ")
                        print("| |   | |  __/ | | (_| |  __/")
                        print("|_|   |_|\___|_|  \__,_|\___|")
                        print("")
                        print("")

    #jugador gana
                if sumaJugador<=21:

                    if sumaJugador>sumaCasa or sumaCasa>21:
                        print("La casa tiene "+str(sumaCasa)+" y el jugador tiene "+str(sumaJugador)+" el jugador")
                        print("")
                        print("  _____                   ")
                        print(" / ____|                  ")
                        print("| |  __  __ _ _ __   __ _ ")
                        print("| | |_ |/ _` | '_ \ / _` |")
                        print("| |__| | (_| | | | | (_| |")
                        print(" \_____|\__,_|_| |_|\__,_|")
                        print("")

                
        game()

                
    
game()



