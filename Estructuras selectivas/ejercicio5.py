#Calcular el numero de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico

import time
print("Femeninio", "Masculino")
sex = input("Genero: ").lower().strip()
edad = int(input("Edad: "))

pulsaciones = 0

while (pulsaciones < 20):
    pulsaciones += 1
    for i in range(1,11):
        print(f"Seg. {i}")
        time.sleep(0.3)
    print(f"Pulsacion {pulsaciones}")

if sex == "Masculino":
    pulsaciones = (220 - edad) / 10
    print(f"El numero de pulsaciones es: {pulsaciones}, por cada 10 segundos")
elif sex == "masculino":
    pulsaciones = (210 - edad) / 10
    print(f"El numero de pulsaciones es: {pulsaciones}, por cada 10 segundos")
else:
    print("Escribe bien brooo")