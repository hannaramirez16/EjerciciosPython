#En una llantera se ha establecido una promocion de las llantas marca "Todo terreno", dicha promocion consisten en lo siguinte: Si se compra menos de 5 llantas el precio es de 300.000

llantas = int(input("¿Cuantas llantas va a comprar?: "))

if llantas < 5:
    llantas *= 300000
    print(f"Esto cuestan las llantas si compras menos de 5: {llantas}")
elif llantas >= 5 and llantas <= 10:
    llantas *= 250000
    print(f"Este es el valor de las llantas si compra más de 5 hasta 10: {llantas}")
elif llantas > 10:
    llantas *= 200000
    print(f"Valor de las llantas si compras mas de 10: {llantas}")
else:
    print("Digita bien el numero")