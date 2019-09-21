valores=int(0)  #aqui le estamos dando la variable de o entero
valor=str("") #aqui queremos saber que tipo de dato es float,int etcc

while True:  #esta es una condicion mientras sea verdadero va a seguir acumulando numeros y si es falso ahi rompe
    valor=input("Pon Un Valor Entero:")
    if valor=="":
        print("INCORRECTO.GRACIAS.") #va imprimir el texto
        break #este codigo es para romper el ciclo si es incorrecto como dice el texto te saca del ciclo

    else:
        valores+=int(valor)  #aqui estamos agregando un valor entero
        entrada="VALOR ACUMULADO: {}" #en este codigo estamos haciendo un texto donde entrada es igual que valor acumulado
        print(entrada.format(valores)) #aqui el codigo de .format va imprimir el texto


#Nombre:Jose Patricio Gomez Calderon
#Fecha:20/09/2019
