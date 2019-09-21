valor=int(input ("PON UN VALOR ENTERO:" )) #aqui el codigo imprimimos el texto y agregamos el numero y ese numero tiene que ser entero gracias al int ese te ayuda a convertir en numero las palabras
esmultiplode3=((valor%3)==0) #aqui queremos saber el residuo de los valores 3,5y 7  y si es igual a 0 
esmultiplode5=((valor%5)==0)
esmultiplode7=((valor%7)==0)

if ((esmultiplode3 and esmultiplode5) or esmultiplode7): # ciclo te va a decir los multiplos que tu vas a poner y si estan mal te va a poner el texto de incorrecto
    print("EXCELENTE") #si se cumple la condicion te va a imprimir este texto
else:
    print("INCORRECTO.MAL!")




#Nombre:Jose Patricio Gomez Calderon
#Fecha:20/09/2019
