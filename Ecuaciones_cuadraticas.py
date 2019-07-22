print ("Este programa resuelve una ecuacion cuadratica de la siguiente forma Ax^2+Bx+c=0")
a = int(input("Digite el primer valor (el de x^2): "))
b = int(input("Digite el segundo valor (el de x): "))
c = int(input("Digite el tercer valor: "))

import numpy as np

if(a==0):
    print ("\nNo es una ecuacion cuadratica")
    if(b==0 and c==0):
        print ("\nLa solucion de Bx+C es 0")
    elif (b == 0):
        print ("\nLa ecuacion no tiene solucion")
    else:
        x1=-(c/b)
        print ("\nLa solucion de", b, "x +", c, " es: ", x1)
else:
    x2=((b*b)-(4*a*c))
    if (x2 <= 0):
        print ("\nLa solucion no existe en los reales")
    elif(x2 > 0):
        x3=((-b)+(np.sqrt(x2)))
        x4=((-b)-(np.sqrt(x2)))
        x5=x3/(2*a)
        x6=x4/(2*a)
        if(a==1):
            if(b<0, c<0):
                print ("\nLas soluciones de x^2 +",b,"+",c," son:\n x1=",x5," y x2=",x6)
            elif(b<0):
                print ("\nLas soluciones de x^2 +",b,"+",c," son:\n x1=",x5," y x2=",x6)
            elif(c<0):
                print ("\nLas soluciones de x^2 +",b,"+",c," son:\n x1=",x5," y x2=",x6)
            else:
                print ("\nLas soluciones de x^2 +",b,"+",c," son:\n x1=",x5," y x2=",x6)
        elif(b==1):
            if(a<0, c<0):
                print ("\nLas soluciones de ",a,"x^2 + x +",c," son:\n x1=",x5," y x2=",x6)
            elif(a<0):
                print ("\nLas soluciones de ",a,"x^2 + x +",c," son:\n x1=",x5," y x2=",x6)
            elif(c<0):
                print ("\nLas soluciones de ",a,"x^2 + x +",c," son:\n x1=",x5," y x2=",x6)
            else:
                print ("\nLas soluciones de ",a,"x^2 + x +",c," son:\n x1=",x5," y x2=",x6)
        elif (a<0, b<0, c<0):
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)
        elif (a<0, b<0):
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)
        elif(a<0, c<0):
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)
        elif (b<0, c<0):
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)
        elif (a<0):
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)
        elif (b<0):
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)
        elif (c<0):
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)
        else:
            print ("\nLas soluciones de ",a,"x^2 +",b,"x +",c," son:\n x1=",x5," y x2=",x6)