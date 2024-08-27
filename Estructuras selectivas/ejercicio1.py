#Determinar si un aprendiz aprueba o desaprueba Algoritmia, sabiendo que aprobara si su promedio de 3 calficaciones es mayor o igual a 70; reprueba en caso contrario.

nu1 = int(input("introduce la primera nota: ")) #Variable para determinar la primera nota
nu2 = int(input("introduce la segunda nota: ")) #Variable para determinar la segunda nota
nu3 = int(input("introduce la tercera nota: ")) #Variable para determinar la tercera nota
prom = (nu1 + nu2 + nu3) /3 #Operación para determinar la suma de todas las nota dividiendo el total en 3
if prom > 70: #Las notas tienen que ser mayor a 70 para poder pasar
    print("Aprobaste ¡FELICIDADES!;") #Impreción valor mayor de 70
else: #Variable
    print("Desaprovado, Esfuerzate más") ##Impreción menor de 70