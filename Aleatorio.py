import random #

Valor1=float(24.5) #aqui estamos diciendole que el valor  es Decimal

def numero(): #definiendo el texto o el valor numero

    Valor2=float(random.randrange(1,10))#el valor 2 va agarrar un numero aleatorio nadamas con que sea decimal

    print(Valor1 + Valor2) #va a sumar los valores
    correo = "la suma de x= {} y  y= {}  es z: {}"
    print(correo.format(Valor1,Valor2,Valor1 + Valor2)) #imprime el texto gracias al .format e imprime los valores que se estan sumando 

numero()

#Jose Patricio Gomez Calderon
#Fecha: 14/09/2019
#Matricula:1852897







