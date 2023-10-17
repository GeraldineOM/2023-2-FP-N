import random

numeros_aleatorios = []
list2 = []
list2 = numeros_aleatorios[0:1]

# Función para almacenar en un vector 50 números enteros con valores de 1 a 20
def puntoA(rango_Inicial, rango_Final):
    for _ in range(50):
        numero_aleatorio = random.randint(rango_Inicial, rango_Final)
        numeros_aleatorios.append(numero_aleatorio)

# Función para imprimir la cantidad de veces que se repiten los números de la segunda función en el primero.
def puntoC(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

# Función para adicionar los números de la primera función sin repetir
def puntoB(lista1, lista2):
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            lista2.append(lista1[i])

# Función para leer un número por teclado e informar cuántas veces se repite en el primer vector
def puntoD(numero, lista):
    cantidad = lista.count(numero)
    return cantidad

# Función para contar cuántos elementos tiene cada una de las listas
def puntoE(lista):
    return len(lista)

while True:
    print("Menú:")
    print("1. Generar números aleatorios")
    print("2. Mostrar lista de números aleatorios")
    print("3. Mostrar lista sin repeticiones")
    print("4. Contar repeticiones en la lista sin repeticiones")
    print("5. Imprimir la cantidad de veces que se repite un valor en la lista sin repeticiones")
    print("6: Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        puntoA(1, 20)
        puntoB(numeros_aleatorios, list2)
        print("Números aleatorios generados y lista sin repeticiones actualizada.")

    elif opcion == "2":
        print("Lista de elementos aleatorios")
        print(numeros_aleatorios)
        print(f"Cantidad de elementos en 'Lista de números aleatorios': {puntoE(numeros_aleatorios)}")

    elif opcion == "3":
        print("Lista sin repeticiones:")
        print(list2)
        print(f"Cantidad de elementos en 'Lista sin repeticiones': {puntoE(list2)}")

    elif opcion == "4":
        numero_a_contar = int(input("Ingrese un número para contar cuántas veces se repite en 'Lista de números aleatorios': "))
        repeticiones = puntoD(numero_a_contar, numeros_aleatorios)
        print(f"El número {numero_a_contar} se repite {repeticiones} veces en 'Lista de números aleatorios'.")

    elif opcion == "5":
        recuentos = puntoC(list2)
        print("Recuento de elementos en lista sin repeticiones")
        for elemento, cantidad in recuentos.items():
            print(f"{elemento}: {cantidad} veces")

    elif opcion == "6":
        print("Programa finalizado")
        break  
    


    else:
        print("Opción no válida. Intente de nuevo.")
