#En un supermercado se hace una promoción, mediante el cual el cliente obtiene un descuento dependiendo de un color que se escoge al azar

import random #Importo la libreria random

colors = ["rojo", "amarillo", "celeste", "rojo", "negro", "blanco", "verde", "morado", "cafe"] #Determinación colores principales

producto = int(input("Valor de tu producto: ")) #Defino el valor de la compra para que usuario digite 
balota = random.choice(colors) #Se escoge un color al azar con el metodo choice


print(f"El color elegido es {balota}") #Se imprime el color sacado de la boleta

if balota == "morado": #Si el valor de la boleta es morado
    descuento = producto * 0.20 #Al producto se le aplica un descuento del 20%
    valorFinal = producto - descuento #Se le resta el descuento
    print(f"El valor de la comrpra {producto}, el color de la balota {balota}, y valor final es {valorFinal}") #Se imprime el valor de la compra
elif balota == "verde": #Si el valor de la boleta es verde
    descuento = int (producto * 0.4) #Al prodcuto se le aplica un descuento del 40%
    valorFinal = producto - descuento #Se le resta el descuento
    print(f"El valor de la compra {producto}, el color de la balota {balota}, y el valor final es {valorFinal}") #Imprimo el valor de la compra
else:
    print(f"El otro color escogido es: {balota}. Por lo tanto, el valor a pagar es {producto}") #Ahora si los valores no son verde ni rojo, se le cobra el porcuto normal
