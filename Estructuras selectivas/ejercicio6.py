#Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: Si el promedio obtenido por un alumno en el ultimo periodo es mayor o igual que 4.0, se le hará un descuento del 30% sobre la pension

nombre = str(input('Ingrese el nombre del estudiante: '))
pension = float(input('¿Cuanto paga por pension?: '))
promedio = float(input('Ingresa el promedio general obtenido: '))
if promedio >= 4.0 and promedio <= 5.0:
    pension *= 0.3
    print(f'Al estudiante {nombre}, se le descuenta un 20% a la pension, por lo cual este seria el pago final {"%.0f" % pension}')
elif promedio < 4.0 and promedio > 0.0:
    iva = pension * 0.2
    pension += iva
    print(f'Al estudiante {nombre}, debera pagar la presión completa con el iva {"%.0f" % pension} ')
else:
    print('Ingresa un numero valido <:')