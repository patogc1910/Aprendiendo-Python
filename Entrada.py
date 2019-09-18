Number=input() #Aqui que pongas el numero
print(type(Number))  #Aqui esta dando que tipo de dato es este programa

print("VALOR:") #aqui estamos imprimiendo el Texto que dice valor


valor_entero=(Number.isdigit() and Number.find(".")==-1)  #aca le estamos diciendo que nadamas podemos poner digitos o numeros con el comando .isdigit y que nos de un numero decimal

if (valor_entero): #aqui estamos pidiendo que si el valor es entero

    print("VALOR ENTERO.EXCELENTE") #aqui que imprima el valor entero,si se cumple la condicion o si el valor es entero
else:
    print("VALOR NO ENTERO.VUELVE A INTENTAR,GRACIAS")  #aqui va imprimir si el valor no es entero, si no se cumple con la condicion si no pones un numero entero te va a salir este texto
