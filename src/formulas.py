import math
#Conversiones
def decimal_to_scientific(decimal_num):
    return "{:.2e}".format(decimal_num)

def decimal_to_scientific_negative(decimal_num):
    return "{:.2e}".format(-decimal_num)

def decimal_to_integer(decimal_num):
    return int(round(decimal_num * 1000))

#Ejercicio 2
def resta_deltaX(deltaX_1, deltaX_2):
    distancia = float(deltaX_1) - float(deltaX_2)
    return distancia

# Formulas de Cinematica Movimiento Rectilineo Uniforme
#Ejercicio 1 y 2
def mru_tiempo(distancia, velocidad):
    tiempo =  distancia / velocidad
    return tiempo

# Formulas de Cinematica Movimiento Rectilineo Uniformemente Acelerado
#Ejercicio 3
def mrua_f1_aceleracion(VF, VI, D):
    return (VF**2 - VI**2) / (2 * D)

def mrua_f3_tiempo(VF, VI, A):
    return (VF - VI) / A

# Ejercicio 4
def mrua_f2_deltaX(VI_1, VI_2, T, A_1, A_2):
    deltaX_1 = (VI_1 * T) + (0.5 * A_1 * (T**2))
    deltaX_2 = (VI_2 * T) + (0.5 * A_2 * (T**2))
    return [deltaX_1, deltaX_2]

def mrua_f2_tiempo(deltaX_1, deltaX_2, distancia_inicial):
    tiempo = 2 * distancia_inicial / deltaX_1 + deltaX_2
    result = math.sqrt(tiempo)
    return result

#Ejercicio 5

def convertir_km_h_A_m_s(km_h):
    return km_h * 1000 / 3600

def mrua_velocidad_final(VF, VI, A):
    T = (VF - VI) / A
    return T
