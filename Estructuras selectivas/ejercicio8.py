#Tomando como base los resultados obtenidos en un laboratorio de analisis clinicos, un medico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo, y en caso contrario como negativo
def main(): #Definicion de la variable como punto de entrada del codigo
    print("¿Cuál es tu tipo de Anemia?") #Se le muestra el presente mensaje al usuario para que coloque la información inicial

    edad_tipo = input("¿Escoge el tipo de edad (Bebe, Niño o Adulto): ").lower().strip() #Definir el tipo de edad del paciente
    
    hemoglobina = float(input("¿Cuál es tu nivel de hemoglobina actual?: ")) #Obtener el nivel de hemoglobina
    
    if edad_tipo == "bebe": #Compara el valor de la variable edad_tipo con la cadena "bebe"
        edad_meses = int(input("¿Cuántos meses tiene el bebé?: ")) #Determinar el rango de hemoglobina basado en la edad y el sexo
        if edad_meses <= 1: #Condicion para determinar si la edad en meses es menor o igual a 1, se asigna un rango de hemoglobina de (13, 26),Este es el rango de hemoglobina esperado para bebés muy jóvenes.
            rango_hemoglobina = (13, 26) #crea una tupla que contiene dos valores numéricos
        elif 2 <= edad_meses <= 6: #Condicion para determinar si la edad en meses está entre 2 y 6 años, se asigna un rango de hemoglobina de (10, 18). Este rango es adecuado para bebés un poco mayores.
            rango_hemoglobina = (10, 18) #crea una tupla que contiene dos valores numéricos
        elif 7 <= edad_meses <= 12: #Condicion para determinar si la edad en meses está entre 7 y 12, se asigna un rango de hemoglobina de (11, 15). Este rango es para bebés que están cerca del primer año de vida.
            rango_hemoglobina = (11, 15) #crea una tupla que contiene dos valores numéricos
        else: #Código a ejecutar si la condición es falsa
            print("Por la edad ya no se denomina Bebé.") #Comentario deteiminando que el niño ya no cumple con la edad de Bebes
            return #Cierre

    elif edad_tipo == "niño": #Este elif se ejecuta si el valor de edad_tipo es igual a "niño". Es una de las posibles condiciones para determinar el rango de hemoglobina basado en el tipo de edad especificado.
        edad_anios = int(input("¿Cuántos años tiene el niño?: ")) #Se solicita al usuario que ingrese la edad del niño en años. La entrada del usuario es convertida a un número entero (int) para su uso en las comparaciones posteriores.
        if 1 <= edad_anios <= 5: #Se verifica si la edad del niño está en el rango de 1 a 5 años, ambos inclusive. Esta condición ayuda a determinar el rango adecuado de hemoglobina para esta franja de edad.
            rango_hemoglobina = (11.5, 15) #Si la condición anterior es verdadera (edad entre 1 y 5 años), se asigna el rango de hemoglobina de (11.5, 15) a la variable rango_hemoglobina. Este rango es considerado normal para esta edad específica.
        elif 6 <= edad_anios <= 10: #Si la edad del niño no está en el rango de 1 a 5 años pero está en el rango de 6 a 10 años, se entra en este elif. Es una condición adicional para evaluar el rango de hemoglobina basado en la nueva franja de edad.
            rango_hemoglobina = (12.6, 15.5) #Si la condición anterior es verdadera (edad entre 6 y 10 años), se asigna el rango de hemoglobina de (12.6, 15.5) a la variable rango_hemoglobina. Este rango es considerado normal para niños de 6 a 10 años.
        elif 11 <= edad_anios <= 15: #Este elif se ejecuta si la edad del niño está en el rango de 11 a 15 años. Si ninguna de las condiciones anteriores es verdadera pero la edad encaja en este rango, se considera esta condición.
            rango_hemoglobina = (13, 15.5) #Si la condición anterior es verdadera (edad entre 1 y 5 años), se asigna el rango de hemoglobina de (11.5, 15) a la variable rango_hemoglobina. Este rango es considerado normal para esta edad específica.
        else: #Código a ejecutar si la condición es falsa
            print("Por la edad ya no se denomina Niño.") #Comentario deteiminando que el niño ya no cumple con la edad de Niño
            return #Cierre

    elif edad_tipo == "Adulto": #Este elif se ejecuta si el valor de edad_tipo es igual a "Adulto"
        sexo = input("¿Cuál es tu sexo? (femenino o masculino): ").lower().strip() #Solicita al usuario que ingrese su sexo, y convierte la entrada a minúsculas usando `.lower()` para estandarizarla.
        if sexo == "femenino": #Verifica si el valor ingresado para el sexo es "femenino".
            rango_hemoglobina = (12,16) # Si el sexo es "femenino", se asigna el rango normal de hemoglobina para mujeres (12 a 16 gramos por decilitro) a la variable `rango_hemoglobina`.
        elif sexo == "masculino": # Verifica si el valor ingresado para el sexo es "masculino".
            rango_hemoglobina = (14,18) #Si el sexo es "masculino", se asigna el rango normal de hemoglobina para hombres (14 a 18 gramos por decilitro) a la variable `rango_hemoglobina`
        else: #Código a ejecutar si la condición es falsa
            print("Sexo inválido.") #Si el sexo ingresado no es válido, se muestra un mensaje y se sale del bloque de código.
            return #Cierre

    else: #Código a ejecutar si la condición es falsa
        print("Tipo de edad inválido.") #Si la edad del usuario es invalida para determinar si se tiene anemia o no
        return #Cierre

    # Evaluar si la hemoglobina está dentro del rango
    if rango_hemoglobina[0] <= hemoglobina <= rango_hemoglobina[1]: 
        print("Negativo para anemia.")
    else: #Código a ejecutar si la condición es falsa
        print("Tus niveles son positivos para anemia. Pide una consulta médica urgente.")
if NameError== "_main_":
    main()