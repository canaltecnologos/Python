# -*- coding: utf-8 -*-
##import numpy as np
#Variables
matriz = []

#Funciones
def mat(n, m):
    for i in range (n):
        matriz.append([])
        for j in range (m):
            matriz[i].append(0)
    return matriz

def llenar(n, m):
    matriz = mat(n, m)
    for x in range (n):
        for y in range (m):
            ##matriz[x][y] = np.random.randint(1, high = 100)  ##números random para pruebas
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + '] = '))
    im(n, m, False)
        
def gauss(n, m):
    for z in range (n-1):
        for x in range(1, n-z):
            if (matriz[z][z] != 0):
                p = matriz[x+z][z] / matriz[z][z]
                for y in range (m):
                    matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
                    
def im(n, m, r):
    if (r):
        print("\nMatriz resultante:")
    else:
        print("\nMatriz inicial: ")
    for i in range (n):
            print (matriz[i][:])

#Programa
n = int(input ('Filas de la matriz : '))
m = int(input ('Columnas de la matriz : '))
while(m < n):
    print("El valor de columnas tiene que ser mayor al de las filas. Por favor ingresa un valor mayor o igual a", n)
    m = int(input ('Columnas de la matriz : '))
llenar(n, m)
gauss(n, m)
im(n, m, True)