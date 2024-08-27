#Calcular el total a pagar por la compra de zapatillas. Si se compran 3 o mas zapatillas se aplica un descuento del 20% sobre el total de la compra y si son menos de 3 zapatillas un descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar  una vez aplicado el descuento

ValueZap = 300000
zap = int(input("Cuantas zapatillas vas a comprar?"))
if zap <3:
    descuent = ValueZap * 0.2
    valueFinal = int (ValueZap - descuent)
    print(f"El valor de tu compra es{ValueZap}, el valor del descuento {descuent}, el valor a pagar es {valueFinal}")
elif zap > 3:
    descuent = ValueZap * 0.3
    valueFinal = int(ValueZap - descuent)
    print(f"el valor de tu compra es {ValueZap}, el valor del descuento es {valueFinal}")