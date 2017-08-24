import random

"""-------------------------------------------------------------------------"""

def pintas(pinta, numero):
    if numero <= 10 and numero > 1:
        return [[numero, pinta]]+pintas(pinta, numero+1)
    else:
        if numero == 1:
            return [["A",pinta]]+pintas(pinta, numero+1)
        else:
            if numero > 10:
                if numero == 11:
                    return [["J", pinta]]+pintas(pinta, numero+1)
                else:
                    if numero == 12:
                        return [["Q", pinta]]+pintas(pinta, numero+1)
                    else:
                        if numero == 13:
                            return [["K", pinta]]+pintas(pinta, numero+1)
                        else:
                            if numero >= 14:
                                return []
                            
"""-------------------------------------------------------------------------"""

def hacerbaraja():
    return pintas("D",1)+pintas("C",1)+pintas("P",1)+pintas("T",1)
                            
"""-------------------------------------------------------------------------"""

def barajar(lista):
    random.shuffle(lista)
    return lista

"""-------------------------------------------------------------------------"""

def primeracarta(lista):
    return [lista.pop(0)]

"""-------------------------------------------------------------------------"""

def sacarvalor(lista):
    if lista[0] == "J" or lista[0] == "Q" or lista[0] == "K":
        return 10
    else:
        if lista[0] == "A":
            return 11
        else:
            return lista[0]

"""-------------------------------------------------------------------------"""

def sacardelista(lista, n, funcion):
    if n < len(lista) and funcion == "sumar":
        return sacarvalor(lista[n])+sacardelista(lista, n+1, funcion)
    else:
        if n < len(lista) and funcion == "aces":
            return contarrecursivo(lista[n], "A")+sacardelista(lista, n+1, funcion)
        else:
            if n >= len(lista):
                return 0

"""-------------------------------------------------------------------------"""

def contarrecursivo(mano, objeto):
    if mano[0] == objeto:
        return 1
    else:
        return 0

"""-------------------------------------------------------------------------"""

def cuentaaces(mano,decision):
    if decision == "si" and sacardelista(mano, 0 , "aces")!=0:
        return (sacardelista(mano,0,"aces")-1)+(sacardelista(mano,0,"sumar")-((sacardelista(mano,0,"aces")-1)*11))
    else:
        if decision == "no" and sacardelista(mano, 0 , "aces")!=0:
            return sacardelista(mano,0,"aces")+(sacardelista(mano,0,"sumar")-(sacardelista(mano,0,"aces")*11))
        else:
            if decision!= "si" or decision!="no":
                return sacardelista(mano,0,"sumar")

"""-------------------------------------------------------------------------"""

def pedirdato(funcion, jugador):
    if funcion == "pedir carta":
        return raw_input("El jugador decea pedir carta S(s) N(no)")
    else:
        if funcion == "que aces":
            return int(input("tiene dos opciones ya que cuenta con aces en su baraja "+ str(cuentaaces(jugador, "si"))+ " o " +str(cuentaaces(jugador, "no"))+" "))
        else:
            return ("No ha elejido un caracter valido para contiuar")

"""-------------------------------------------------------------------------"""

def verificaropcion(opcion, jugador):
    if opcion == cuentaaces(jugador, "si"):
        return cuentaaces(jugador, "si")
    else:
        if opcion == cuentaaces(jugador, "no"):
            return cuentaaces(jugador, "no")
        else:
            return verificaropcion(pedirdato("que aces", jugador),jugador)

"""-------------------------------------------------------------------------"""

def conacesocinaces(jugador):
    if sacardelista(jugador,0,"aces") >= 1:
        return verificaropcion(pedirdato("que aces", jugador),jugador)
    else:
        if sacardelista(jugador,0,"aces") == 0:
            return cuentaaces(jugador, "no hay nada")

"""-------------------------------------------------------------------------"""

def verificar21(sumatoria,jugador, baraja):
    if sumatoria < 21:
        return pedircarta(jugador,baraja,pedirdato("pedir carta", jugador))
    else:
        if sumatoria == 21:
            return 21
        else:
            if sumatoria > 21:
                return 22

"""-------------------------------------------------------------------------"""

def pedircarta(jugador, baraja, funcion):
    if funcion == "S":
        return jugador.extend(primeracarta(baraja))
    else:
        if funcion == "N":
            return False
        else:
            return pedircarta(jugador, baraja, pedirdato("pedir carta", jugador))

"""-------------------------------------------------------------------------"""

def repetir(jugador,baraja , funcion):
    if funcion == False:
        return conacesocinaces(jugador)
    else:
        if funcion > 21:
            print ("creo que te has pasado")
            return 22
        else:
            if funcion == 21:
                print ("enhorabuena tienes veintiuna")
                return 21
            else:
                print (jugador)
                return repetir(jugador, baraja, verificar21(conacesocinaces(jugador),jugador, baraja))

"""-------------------------------------------------------------------------"""

def IA(casa, baraja, juegojugador):
    if sumarIA(casa) < juegojugador and juegojugador <= 21:
       casa.extend(primeracarta(baraja))
       print (casa)
       print (sumarIA(casa))
       return IA(casa, baraja, juegojugador)
    else:
        return comparar(juegojugador,sumarIA(casa))
    
"""-------------------------------------------------------------------------"""

def sumarIA(casa):
    if sacardelista(casa,0,"aces") >= 1:
        if (cuentaaces(casa, "si") >= cuentaaces(casa, "no")) and cuentaaces(casa, "si") <= 21:
            print (cuentaaces(casa, "si"))
            return cuentaaces(casa, "si")
        else:
            return cuentaaces(casa, "no")
    else:
        if sacardelista(casa,0,"aces") < 1:
            print (cuentaaces(casa, "no hay nada"))
            return cuentaaces(casa, "no hay nada")

"""-------------------------------------------------------------------------"""

def comparar(juegojugador, juegocasa):
    if juegojugador < juegocasa and (juegocasa <= 21 and juegojugador <= 21):
        return "juego para la casa"
    else:
        if juegojugador > juegocasa and (juegocasa <= 21 and juegojugador <= 21):
            return "juego para el jugador"
        else:
            if juegojugador == juegocasa and (juegocasa <= 21 and juegojugador <= 21):
                return "juego en empate"
            else:
                if juegojugador <= 21 and juegocasa > 21:
                    return "juego para el jugador "
                else:
                    if juegojugador > 21 and juegocasa <= 21:
                        return "juego para la casa"

"""-------------------------------------------------------------------------"""

def juego(baraja, casa , jugador):
    if raw_input(" El jugador quiere jugar S(si) N(no) ") == "S":
        barajar(baraja)
        jugador.extend(primeracarta(baraja))
        casa.extend(primeracarta(baraja))
        jugador.extend(primeracarta(baraja))
        casa.extend(primeracarta(baraja))
        print ("la mano del jugador es "+str(jugador))
        print ("la mano de la casa es "+str(casa[0]))
        print (IA(casa, baraja, repetir(jugador, baraja, verificar21(conacesocinaces(jugador),jugador, baraja))))
        print ("mano final del jugador"+str(jugador))
        print ("mano final de la casa"+str(casa))
        return juego(hacerbaraja(),[],[])
    else:
        print ("hasta luego")

"""-------------------------------------------------------------------------"""

juego(hacerbaraja(),[],[])
