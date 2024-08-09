#variable
print("Tu compra tiene un descuento del 40%") #Se define el descuento que se ofrece para el valor total de la compra
compra = int(input("Ingresa el costo del valor de tu compra: ")) #Se ingresa en esta variable el valor total de toda la compra sin el descuento
descuento = compra * 0.5 #En esta variable se refleja la operación para sacar el valor total
print(f"La compra fue de ¨{compra}, con un descuento del {descuento}") #El mensaje que aparece antes de que aparezca el valor total de la compra con el descuento
compra -= descuento #Variable donde se ve el valor total y el descuento que se aplica
print(f"El valor final a pagar de su compra es: {compra} ") # El mensaje final mostrando el valor final de toda la operacion