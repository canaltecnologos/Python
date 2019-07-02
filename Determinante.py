# -*- coding: utf-8 -*-

#Variables
matriz = []

#Funciones
def mat(n):
    for i in range (n):
        matriz.append([])
        for j in range (n):
            matriz[i].append(0)
    return matriz

def llenar(n):
    matriz = mat(n)
    for x in range (n):
        for y in range (n):
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + '] = '))
        
def gauss(n):
    for z in range (n-1):
        for x in range(1, n-z):
            if (matriz[z][z] != 0 ):
                p = matriz[x+z][z] / matriz[z][z]
                for y in range (n):
                    matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
                    
def det(n):
    deter=1
    for x in range (n):
        deter=matriz[x][x]*deter
    print ('\nEl determinante de la matriz es = ', deter)
                    
def im(n):
    print("\nMatriz resultante:")
    for i in range (n):
            print (matriz[i][:])

#Programa
n = int(input ('Tamano de la matriz : '))
llenar(n)
gauss(n)
det(n)
im(n)