__author__ = 'danielalorenzo'

import random

class Maleantes():
    def __init__(self):
        self.nombre = ""
        self.vida = ""
        self.posicion = ""
        self.chivato = ""
        self.coste = ""
        self.ganancia = ""

def createMalos():
    lista_malos = list()
    for i in range(0,20):
        malo = Maleantes()
        malo.id = i
        malo.nombre = 'malo_'+str(i)
        malo.vida = random.randrange(1,20)
        malo.posicion = random.randrange(1,20)
        malo.chivato = bool(random.getrandbits(1))
        malo.coste = random.randrange(1,20)
        malo.ganancia = random.randrange(1,100)
        lista_malos.append(malo)
    return lista_malos

def ordenarPosicion(malos):
    malos_orden = sorted(malos, key=lambda mi_malo: mi_malo.posicion)
    return malos_orden

def crearHorario(malos):
    horas_dia = 24
    horas_prev = 0
    dia = 0
    semana = list()
    ganancias = 0
    coste = 0

    for malo in malos:
        if not (malo.chivato):
            semana.append(malo.nombre)
            ganancias += malo.ganancia
            coste += malo.coste
            horas_dia -= malo.vida

            while (horas_dia < 0):
                if (dia < 6):
                    horas_prev = 24 + horas_dia
                    horas_dia = horas_prev
                    horas_prev = 24
                    print '--------'
                    print 'Dia: '+str(dia)
                    print '--------'
                    imprimir(semana)
                    semana = list()
                    dia += 1
                    semana.append(malo.nombre)

    print '--------'
    print 'Dia: '+str(dia)
    print '--------'
    imprimir(semana)
    semana = list()
    print 'Ganancias: '+str(ganancias)
    print 'Coste: '+str(coste)

def imprimir(horario):
    for i in horario:
        print i
        print ;

def main():

    horas_total = 168
    malos = []
    malosOrden = []
    horario = []

    malos = createMalos()
    malosOrden = ordenarPosicion(malos)

    for i in malosOrden:
        print '--------------------'
        print 'Nombre: '
        print i.nombre
        print 'Vida: '
        print i.vida
        print 'Posicion: '
        print i.posicion
        print 'Chivato: '
        print i.chivato
        print 'Coste: '
        print i.coste
        print 'Ganancia: '
        print i.ganancia
        print '--------------------'

    crearHorario(malosOrden)

main()