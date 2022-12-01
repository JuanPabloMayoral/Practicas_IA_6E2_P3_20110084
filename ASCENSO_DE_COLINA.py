# Juan Pablo Mayoral López 20110084 6E2
# Practica 5 - Ejemplo del algoritmo de ascenso de la colina

import math
import random

def distancia(coord1, coord2):
    lat1=coord1[0]
    lon1=coord1[1]
    lat2=coord2[0]
    lon2=coord2[1]
    return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)

#Calcular distancia

def evalua_ruta(ruta):
    total=0
    for i in range(0,len(ruta)-1):
        ciudad1=ruta[i]
        ciudad2=ruta[i+1]
        total=total+distancia(coord[ciudad1],coord[ciudad2])
        ciudad1=ruta[i+1]
        ciudad2=ruta[0]
        total=total+distancia(coord[ciudad1],coord[ciudad2])
        return total

    def i_hill_climbing():
        #Aqui se crea una ruta inicial aleatoria
        ruta=[]
        for ciudad in coord:
            ruta.append(ciudad)
            mejor_ruta=ruta[:]
            max_iteraciones=10

            while max_iteraciones>0:
                mejora=True
                #Se genera una nueva ruta
                random.shuffle(ruta)
                while mejora:
                    mejora=False
                    dist_actual=evalua_ruta(ruta)
                    #evaluar los vecinos
                    for i in range(0,len(ruta)):
                        if mejora:
                            break
                        for j in range(0,len(ruta)):
                            if i !=j :
                                ruta_tmp=ruta[:]
                                ciudad_tmp=ruta_tmp[i]
                                ruta_tmp[i]=ruta_tmp[j]
                                ruta_tmp[j]=ciudad_tmp
                                dist=evalua_ruta(ruta_tmp)
                                if dist<dist_actual:
                                    #Se encuentra el vecino para mejorar el resultado
                                    mejora=True
                                    ruta=ruta_tmp[:]
                                    break
                max_iteraciones=max_iteraciones-1
                if evalua_ruta(ruta)<evalua_ruta(mejor_ruta):
                    mejor_ruta=ruta[:]

            return mejor_ruta


        coord={
            'Guadalajara':[36.43,-4.24],
            'Vallarta':[37.23,-5.59],
            'Zacatecas':[37.11,-3.25],
            'Aguascalientes':[39.28,-0.22],
            'Colima':[40.24,-3.41]
            }


        ruta= i_hill_climbing()
        print(ruta)
        print("Distancia total: "+str(evalua_ruta(ruta)))
