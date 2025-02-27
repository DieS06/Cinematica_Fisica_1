import math
from formulas import *

def menu ():
    while True:
        print("1.- Ejercicio 1, Rapidez de un impulso nervioso")
        print("2.- Ejercicio 2, Crecimiento del cabello")
        print("3.- Ejercicio 3, Aceleración de un electrón")
        print("4.- Ejercicio 4, Pilotos de carritos")
        print("5.- Ejercicio 5, Tren, tiempo perdido")
        print("0.- Salir\n")

        try:
            opcion = int(input("Selecciona una opcion: "))
            if opcion == 1:
                print ("La rapidez de un impulso nervioso en el cuerpo humano es de aproximadamente 100 m/s.\n     Si su dedo del pie tropieza accidentalmente en la oscuridad\n     ¿Cuanto tiempo cree que tarda el impulso nervioso en viajar a su cerebro?\n")
                print ("¡FORMATO PARA LA ALTURA: 1.75! \n")
                distancia = float(input("Ingrese la altura de la persona: "))
                print("")
                velocidad = 100

                result = mru_tiempo( distancia, velocidad )
                result = decimal_to_integer(result)

                print(f"El tiempo que tarda el impulso nervioso en viajar a su cerebro es de {result} segundos.\n")
            elif opcion == 2:
                print ("El cabello corto crece a una tasa aproximada de 2 cm/mes. \n     Ingrese los datos solicitados a continuación para calcular el tiempo que tarda el cabello en crecer.\n     ¿Cuánto tiempo transcurrirá hasta su suguiente visita al peluquero?\n")

                longitud_inicial = input("Ingrese la longitud inicial del cabello: ")
                print("")
                longitud_final = input ("Ingrese la longitud final del cabello: ")
                print("")
                distancia = resta_deltaX(longitud_final, longitud_inicial)

                result = mru_tiempo(distancia, 2)
                
                if result == 1:
                    result = int(result)
                    print(f"El tiempo que tarda el cabello en crecer es de {result} mes.\n")
                elif result == 12:
                    print(f"El tiempo que tarda el cabello en crecer es de 1 año.\n")
                elif result > 12:
                    result = int(result / 12)
                    print(f"El tiempo que tarda el cabello en crecer es aproximadamente de {result} años.\n")
                else:
                    result = int(result)
                    print(f"El tiempo que tarda el cabello en crecer es aproximadamente de {result} meses.\n")
            elif opcion == 3:
                print ("Un electrón en un tubo de rayos catódicos acelera uniformemente desde una rapidez 2.00x10^4 m/s a 6.00x10^6 m/s en 1.50 cm.\n     a. ¿En qué intervalo de tiempo el electròn recorre estos 1.50 cm?\n     b. ¿Cuàl es su aceleración?")
                print("")
                velocidad_inicial = 2.00e+4
                velocidad_final = 6.00e+6
                distancia = 0.015

                aceleracion = mrua_f1_aceleracion(velocidad_inicial, velocidad_final, distancia)
                tiempo = mrua_f3_tiempo(velocidad_final, velocidad_inicial, aceleracion)

                aceleracion = decimal_to_scientific(aceleracion)
                tiempo = decimal_to_scientific_negative(tiempo)

                print(f"a. El electrón recorre 1.50 cm en un intervalo de tiempo de {tiempo} segundos.\n")
                print(f"b. La aceleración del electrón es de {aceleracion} m/s^2.")
                print("")    
            elif opcion == 4:
                print ("Dos pilotos de carritos están separados por una distancia inicial en una pista larga y recta, mirando en direcciones opuestas.\n")
                distancia_inicial = float(input("Ingrese la distancia inicial entre los carritos: "))
                print("")
                print("Ambos parten al mismo tiempo y aceleran con una tasa constante de m/s^2.\n")

                A_1 = float(input("Ingrese la velocidad inicial del primer carrito: "))
                print("")
                A_2 = float(input("Ingrese la velocidad inicial del segundo carrito: "))
                print("")

                print("¿Qué separación tendrán los carritos luego de 3.0 s?")
                VI_1 = 0
                VI_2 = VI_1
                T = 3
                deltaX = mrua_f2_deltaX(VI_1, VI_2, T, A_1, A_2)
                distancia_final = resta_deltaX(deltaX[0], deltaX[1])
                print(f"La separación entre los carritos luego de 3.0 s es de {distancia_final} m.\n")

                print("¿Cuánto tiempo le toma a los pilotos toparse en la pista?")
                tiempo = mrua_f2_tiempo(deltaX[0], deltaX[1], distancia_inicial)
                tiempo = round(tiempo, 2)
                print(f"El tiempo que le toma a los pilotos toparse en la pista es de {tiempo} s.\n")
            elif opcion == 5:
                print ("Un tren normalmente viaja con rapidez uniforme de 72km/h por un tramo largo de vía recta y plana.\nCierto día, el tren debe hacer una parada de 2 minutos en una estación sobre la vía.\nSi el tren desacelera con una tasa uniforme de 1.0 m/s^2 y, después de la parada, acelera con una tasa de 0.5m/s^2.\n")
                VI = convertir_km_h_A_m_s(72)
                VF = 0
                A = -1

                print("¿Cuánto tiempo tarda el tren en detenerse?")
                T1 = mrua_f3_tiempo(VF, VI, A)
                T1 = round(T1, 2)
                print(f"El tren tarda {T1} s en detenerse.\n")

                print("¿Cuánto tiempo tarda el tren en acelerar de nuevo hasta su rapidez original?")
                A = 0.5
                VF = convertir_km_h_A_m_s(72)
                VI = 0
                T2 = mrua_velocidad_final(VF, VI, A)
                T2 = round(T2, 2)
                print(f"El tren tarda {T2} s en acelerar de nuevo hasta su rapidez original.\n")

                print("¿Cuánto tiempo hábra perdido por parar en la estación?")
                tiempo_perdido = T1 + 120 + T2
                tiempo_perdido = round(tiempo_perdido, 2)
                print(f"El tren habrá perdido {tiempo_perdido} s por parar en la estación.\n")

            elif opcion == 0:
                print("¡Programa terminado!")
                break
            else:
                print("Opcion no valida. Intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número válido.")


def main():
    menu()

if __name__ == '__main__':
    main()

