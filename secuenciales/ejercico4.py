#variable
nombre_del_Vendedor = str (input("Ingres a tu nombre: ")) #se define en esta variable el nombre del vendedor el cual tiene que colocar el vendedor
sueldo_del_vendedor = int (input("Ingresa el valor de tu sueldo: ")) #Se define en esta variable el sueldo del vendedor el cual tiene que colocar el vendedor
valor_comision = int (input("Ingresa tus comisiones: ")) #se define en esta variable el valor de las comisiones del vendedor el cual tiene que colocar el vendedor
sueldo_Final_del_vendedor = sueldo_del_vendedor + valor_comision #Se define el valor total de la suma de los tres porcetajes de las variables anteriores
print(f"El vendedor{nombre_del_Vendedor}, tiene un sueldo de {sueldo_del_vendedor}, durante el mes obtuvo una comision de {valor_comision}\n El valor final de su sueldo es de: ") #El mensaje final que se le colocar para que se vea el valor total de la operación
