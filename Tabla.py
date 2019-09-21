Tabla=input("Dame el Number del 0 al 10: ")  # aqui vamos a imprimir el texto , vamos a ponerle el numero que queramos
Tabla=int(Tabla)    #en el operador int le estamos diciendo que  lo vamos a convertir en un numero entero 

for a in range(0 , 12):    #aqui estamos dandole un ciclo que por ejemplo nosotros ponemos el numero pero gracias a eso  el operador le esta dando escoger del 0 al 12

    entrada= "{} x {} = {}"   #aqui estamos poniendo corchetes por que adentro de los corchetes va hacer lo que pongamos nosotros de numero
    print(entrada.format(Tabla,a,Tabla*a))  #gracias al .format nos da todo el texto donde esta el codigo de entrada  y nos va a imprimir el numero que escogamos gracias al input  y la maquina va a poner del 0 al 12 gracias al operador for 
    
    
   # Nombre:Jose Patricio Gomez Calderon
   # Fecha:20/09/2019
    
