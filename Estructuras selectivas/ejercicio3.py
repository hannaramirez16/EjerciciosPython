#Una empresa quiere hacer una compra de varias piezas de la misma clase a una fabrica de bolsos. La empresa, dependiendo del monto total de la compra, decidira que hacer para pagar al fabricante (...)

montoTotal = int(input('Ingresa el monto total de la compra: ')) #Se coloca la variable montoTotal
if montoTotal > 400000: #Condicional para determinar si el monto total es mayor de 400000
    inversion = int (montoTotal * 0.55)  #Se declara la variable inversion tipo int
    prestamos = int (montoTotal * 0.4) #Declaro los préstamos, aumentando mi monto total en un 30%
    restanteCredito = int (montoTotal * 0.15) #También declaro el crédito restante para aplicar un descuento del 15%
    print(f'Valor invertido {inversion}, el valor prestado al banco es de: {prestamos} y el valor del credito del fabricante es {restanteCredito}') #Imprimo los diferentes valores, y si el montoTotal es menor a 400,000, se toma una acción específica
    inversion = int (montoTotal * 0.7) #Se declara la inversión y se calcula el 70% de la misma
    credito = int (montoTotal * 0.3) #Se declara el crédito y se calcula el 30% del mismo
    intereses = int (credito * 0.2) #Se declara el monto de intereses y se calcula el 20% del mismo
    credito += intereses #Se suman los intereses al monto principal
    print(f'Valor invertido: {inversion}, valor de credito al fabricante {credito} (A el credito se le cobran estos intereses {intereses})') #Imprimo los valores
else:
    print('Ocurrio una equivocación')