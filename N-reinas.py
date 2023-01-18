# Juego de N reinas
##################################################
# n reinas
# r celdas
# (n+1)**r*r
# ###############################################  

# Declaración de librerias
##################################################

import os, sys, copy, time, numpy as np

# Declaración de variables
##################################################

limpia_pantalla = 'clear' if os.name == 'posix' else 'CLS'
celdas = 0
reinas = 0
#tablero = []
estado_inicial = []
estado_actual = []
movimiento_actual = 0

# Declaración de funciones
##################################################

def Reset():
    global celdas, reinas, estado_actual,estado_inicial #,tablero

    celdas = 0
    reinas = 0
    estado_inicial = []
    estado_actual = []

def Peticion_variables():
    global celdas, reinas, estado_inicial

    os.system(limpia_pantalla)
    print('\n================================================')
    print('Bienvenidos al juego de las N reinas v0.1')
    print('================================================\n')

    while celdas == 0 or not celdas.isnumeric():
        celdas = input('Introduce el tamaño del tablero, NxN celdas : (Recomendado no más de 4): ')
    celdas = int(celdas)
    while reinas == 0 or not reinas.isnumeric():
        reinas = input('Introduce el número de reinas (Recomendado no más de 4): ')
    reinas = int(reinas)

    estado_inicial = np.zeros((celdas,celdas), dtype=int)

    # count = 3
    # print('Empezando en :')
    # for x in range(count,0, -1):
    #     print(x,'...')
    #     time.sleep(1)

def Imprime_estado():
    os.system(limpia_pantalla)
    print('\n====================')
    print('   N reinas v0.1')
    print('====================\n')
    print('Celdas : ',celdas,' x ',celdas)
    print('Reinas: ',reinas)
    print('====================\n')

    x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in estado_inicial])
    #x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in estado_actual])
    print(x)


########### COMPROBAR ###########################

def Comprueba_estado(state):
    #assert type(state)== list and len(state)==celdas
    def es_valido(t):
        for n in range(len(t)-1):
            if(t[n]>t[n+1]):
                return False
        return True
    def comprueba_reinas(s):
        for x in range(len(s)):
            if not es_valido(s[x]):
                return False
        return True
    if comprueba_reinas(state):
        return True
    else:
        return False

def Estados(s):
    for x_celdas in range(len(s)[0]):
        for y_celdas in range(len(s)):
            ns=copy.deepcopy(s)
            if add_torre != del_torre and ns[del_torre]:
                ns[add_torre].insert(0,ns[del_torre][0])
                ns[del_torre].pop(0)
                yield ns

def Profundidad(actual, path=[]):
    if actual==estado_final:
        return [actual]
    else: 
        for ns in Estados(actual):
            if Comprueba_estado(ns) and ns not in cerrados:
                cerrados.append(ns)
                r=Profundidad(ns,cerrados)
                if r:
                    r.insert(0,actual)
                    return r
        return []

def Ejecucion_total():
    global estado_actual,movimiento_actual
    try:
        Reset()
        Peticion_variables()
        #solucion = Profundidad(estado_inicial)
        Imprime_estado()
        # for paso in solucion:
        #     estado_actual = paso
        #     Imprime_estado()
        #     movimiento_actual += 1
    except RecursionError:
        print('Disculpe las molestias pero con los parámetros introducimos, se excede la capacidad de cómputo del intérprete.\nPor favor, vuelva a introducir nuevos parámetros con valores más bajos de Discos y/o Torres.')
        input('Pulse cualquier tecla para continuar...')
        Ejecucion_total()

# MAIN CODE
##################################################

Ejecucion_total()