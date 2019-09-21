valor1=input("Pon El Valor1:") #aqui vamos agregar el valor 1
valor2=input("Pon El valor2:") #aqui vamos a poner el valor 2
entrada= "El valor mayor es {} " #este comando es para que imprima el texto del codigo entrada 

if (valor1==valor2): #aqui es una condicional si el valor1 es igual a valor 2 
    print(entrada.format,(valor1,valor2,"ESTOS VALORES SON IGUALES")) #aqui nos va imprimir el texto del codigo entrada y si la condicional cumple pues como dice el texto los valores son iguales

else:
    print()


    if (valor1>valor2): #aqui es una condicional que si el valor 1 es mayor que el dos 

        print(entrada.format,(valor1,valor2,"EL VALOR 1 ES MAYOR QUE EL VALOR2")) 

    else: #aqui igual es una condicional que si el valor 2 es mayor que 1

        print(entrada.format,(valor1,valor2,"EL VALOR 2 ES MAYOR QUE EL VALOR 1"))
        
#Nombre:Jose Patricio Gomez Calderon
#Fecha:20/09/2019
