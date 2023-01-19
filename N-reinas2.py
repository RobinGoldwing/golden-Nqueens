# Juego de N reinas
##################################################
# n reinas
# r celdas
# (n+1)**r*r
# ###############################################  

# Declaración de librerias
##################################################

import os, sys, copy, time, random

# Declaración de variables
##################################################

version = 'v0.2'

limpia_pantalla = 'clear' if os.name == 'posix' else 'CLS'
celdas = 0
reinas = 0
#tablero = []
estado_inicial = []
estado_actual = []
cerrados=[]
iteracion = 0


# Declaración de funciones
##################################################

def Reset():
    global celdas, reinas, estado_actual,estado_inicial, iteracion, speed #,tablero

    celdas = 0
    reinas = 0
    estado_inicial = []
    estado_actual = []
    iteracion = 0
    speed = 0
    cerrados=[]

def Peticion_variables():
    global celdas, reinas, estado_inicial, estado_actual, speed

    os.system(limpia_pantalla)
    print('\n====================')
    print('  N reinas   ',version)
    print('====================\n')

    print('Bienvenidos al juego de las N reinas \n')

    while celdas == 0 or not celdas.isnumeric():
        celdas = input('Introduce el tamaño del tablero, NxN celdas : (Recomendado no más de 4): ')
    celdas = int(celdas)
    while reinas == 0 or not reinas.isnumeric():
        reinas = input('Introduce el número de reinas (Recomendado no más de 4): ')
    reinas = int(reinas)

    while speed == 0 or not speed.isnumeric():
        print('Introduce la velocidad (recomendado de 1 a 30+) : ', end='')
        speed = input()
    speed = float(speed)

    for x in range(celdas):
        estado_inicial.append([])
        for y in range(celdas):
            estado_inicial[x].append(0)

    estado_actual = copy.deepcopy(estado_inicial)

    count = 3
    print('Empezando en :')
    for x in range(count,0, -1):
        print(x,'...')
        time.sleep(1)

def Imprime_estado(state):
    os.system(limpia_pantalla)
    print('\n====================')
    print('  N reinas   ',version)
    print('====================\n')
    print('Celdas : ',celdas,' x ',celdas)
    print('Reinas: ',reinas)
    print('\n====================\n')

    for x in range(len(state)):
        for y in range(len(state[x])):
            print(state[x][y],end=' ')
        print()
    print()
    print('Iteraciones : ',iteracion)
    print()
    time.sleep(1/speed)


def comprueba_filas(state):
    for x in range(len(state)):
        count = 0
        for y in range(len(state[x])):
            count += state[x][y]
        if count > 1: return False
    return True

def comprueba_columnas(state):
    for x in range(len(state)):
        count = 0
        for y in range(len(state[x])):
            count += state[y][x]
        if count > 1: return False
    return True

def comprueba_diagonales_der(state):    
    for x in range(len(state)):
        for y in range(len(state)):
            count=0
            for z in range(len(state)):
                try:
                    count += state[z+x][z+y]
                except:
                    pass
            if count > 1: return False
    return True

def inversa(state):
    inversa = copy.deepcopy(state)
    for x in range(len(state)):
        for y in range(len(state[x])):
            inversa[x][y] = state[x][-y-1]
    return inversa

def comprueba_diagonales_izq(state):
    if comprueba_diagonales_der(inversa(state)): return True
    else:                                        return False

def Comprueba_estado(state):
    #assert type(state)== list and len(state)==celdas
    if comprueba_filas(state) and comprueba_columnas(state) and comprueba_diagonales_der(state) and comprueba_diagonales_izq(state):
        return True
    else:
        return False


# def Diagonal(lista, desplazamiento=0):
#     start = 0 if desplazamiento >=0 else 0 - desplazamiento
#     return [lista[x][x+desplazamiento] for x in range(start,len(lista)-(abs(desplazamiento)-start))]

def Cuenta_reinas(state):
    count = 0
    for x in range(len(state)):
        for y in range(len(state)):
            count += state[x][y]
    return count


########### COMPROBAR ###########################

def Estados(s):
    while Cuenta_reinas(s) != reinas:
        ns=copy.deepcopy(s)
        x = random.randint(0,len(estado_actual)-1)
        y = random.randint(0,len(estado_actual)-1)
        if ns[x][y] == 0:
            ns[x][y] = 1
            yield ns


def Profundidad(actual, path=[]):
    global iteracion
    if Cuenta_reinas(actual) == reinas:
        return [actual]
    else: 
        for ns in Estados(actual):
            iteracion += 1
            # print('Iteración nº : ',iteracion,end='\r')
            # time.sleep(0.2)
            Imprime_estado(ns)
            if Comprueba_estado(ns) and ns not in cerrados:
                cerrados.append(ns)
                r=Profundidad(ns,cerrados)
                if r:
                    r.insert(0,actual)
                    return r
        return []

def Ejecucion_total():
    global estado_actual,iteracion
    try:
        Reset()
        Peticion_variables()
        solucion = Profundidad(estado_inicial)
        #Imprime_estado(estado_inicial)
        # for paso in solucion:
        #     estado_actual = paso
        #     Imprime_estado(estado_actual)
        print('\nConseguido!!\n')
    except RecursionError:
        print('Disculpe las molestias pero con los parámetros introducimos, se excede la capacidad de cómputo del intérprete.\nPor favor, vuelva a introducir nuevos parámetros con valores más bajos de Discos y/o Torres.')
        input('Pulse cualquier tecla para continuar...')
        Ejecucion_total()

# MAIN CODE
##################################################

Ejecucion_total()