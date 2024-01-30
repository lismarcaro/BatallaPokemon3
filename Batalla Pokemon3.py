#Batalla pokemon

import random #para RandRage (elegir ataque oponente)

jugador = [100, 100]   #0 es vida, 1 es defensa
oponente = [100, 100]  #0 es vida, 1 es defensa
ataque_oponente = 1

Ataques = ("latigo", "placaje", "Pistola de agua", "ascuas", "malicioso")
ataque1 = (10, 10)
ataque2 = (29, 31)
ataque3 = (18, 21)
ataque4 = (9, 11)
ataque5 = (5, 32)



while jugador[0] > 0 and oponente[0] > 0:
    ataque_oponente = random.randrange (1,5)
    print("Escoje tu nuevo ataque")
    print("Los ataques son: latigo, placaje, pistola de agua, ascuas y malicioso")
    ataque_jugador = input("ataque: ")
##    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador == "malicioso":
        oponente[1] -= ataque5[1]
        print("Tu ataque es: ")
        print(Ataques[4])
        print(f'La vida del oponente es {oponente[0]}')
    

    if ataque_jugador == "latigo": #latigo
        oponente[1] -=  ataque1[1]
        oponente[0] -= ataque1[0]
        print("Tu ataque es: ")
        print(Ataques[0])
        print(f'La vida del oponente es {oponente[0]}')

        if oponente[1] <= 0:
            oponente[1] = 1
    elif ataque_jugador == "placaje":
        print("Tu ataque es: ")
        print(Ataques[1])
        oponente[0] -= ataque2[1] * (100/oponente[1])
        print(f'La vida del oponente es {oponente[0]}')

    elif ataque_jugador == "pistola de agua": #Pistola de agua
        print("Tu ataque es: ")
        print(Ataques[2])
        oponente[0] -= ataque3[0]
        print(f'La vida del oponente es {oponente[0]}')

    elif ataque_jugador == "ascuas":
        print("Tu ataque es: ")
        print(Ataques[3])
        print(f'La vida del oponente es {oponente[0]}')
        pass


        #Turno del Oponente, se define con un Random

    
    if ataque_oponente == 1: #latigo
        jugador[1] -=  ataque1[1]
        jugador[0] -= ataque1[0]
        print("El ataque de tu oponente es: ")
        print(Ataques[0])
        print(f'Tu vida es {jugador[0]}')
        

    elif ataque_oponente == 2: #placaje
        jugador[0] -= ataque2[1] * (100/jugador[1])
        print("El ataque de tu oponente es: ")
        print(Ataques[1])
        print(f'Tu vida es {jugador[0]}')

        
    elif ataque_oponente == 3: #Pistola de agua
        jugador[0] -= ataque3[0]
        print("El ataque de tu oponente es: ")
        print(Ataques[2])
        print(f'Tu vida es {jugador[0]}')

    elif ataque_oponente == 4: #ascuas
        print("El ataque de tu oponente es: ")
        print(Ataques[3])
        print(f'Tu vida es {jugador[0]}')
        pass

    elif ataque_oponente == 5: #malicioso
        jugador[1] -= ataque5[1]
        print("El ataque de tu oponente es: ")
        print(Ataques[4])
        print(f'Tu vida es {jugador[0]}')
      
    
    else:
        print("¿¡QUE HACES!? Tus ataques son malicioso, placaje y ascuas")
        continue
        
   


#Si términa el ciclo, alguien ganó
if oponente[0] <= 0 and jugador[0] <= 0:
    print("EMPATE")
elif oponente[0] <= 0: #el jugador es >0
    print("PERDISTE")
