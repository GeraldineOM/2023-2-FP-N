import random

def matriz_aleatoria(filas, columnas, min_valor, max_valor):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero_aleatorio = random.randint(min_valor, max_valor)
            fila.append(numero_aleatorio)
        matriz.append(fila)
    return matriz

def segunda_matriz(matriz_uno):
    matriz_dos = [[0] * len(matriz_uno[0]) for _ in range(len(matriz_uno))]

    for columna in range(len(matriz_uno[0])):
        for fila in range(len(matriz_uno)):
            if columna == 0:
                matriz_dos[fila][columna] = matriz_uno[fila][columna] ** 2
            elif columna == 1:
                matriz_dos[fila][columna] = matriz_uno[fila][columna] ** 4
            else:
                matriz_dos[fila][columna] = matriz_uno[fila][columna]

    return matriz_dos

def sumar_filas(matriz):
    vector = []
    for fila in matriz:
        suma_fila = sum(fila)
        vector.append(suma_fila)
    return vector

def sumar_columnas(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    vector_ = [0] * num_columnas
    for columna in range(num_columnas):
        suma_columna = 0
        for fila in range(num_filas):
            suma_columna += matriz[fila][columna]
        vector_[columna] = suma_columna
    return vector_

def matriz_diferencia(matriz_1, matriz_2):
    if len(matriz_1) != len(matriz_2) or len(matriz_1[0]) != len(matriz_2[0]):
        raise ValueError("LAS MATRICES DEBEN SER DEL MISMO TAMAÑO ")
    resultado = [[0 for _ in range(len(matriz_1[0]))] for _ in range(len(matriz_1))]
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[0])):
            resultado[i][j] = matriz_2[i][j] - matriz_1[i][j]
    return resultado

def producto_matriz(matriz, numero):
    x = []
    for fila in matriz:
        fila_resultado = []
        for elemento in fila:
            producto = elemento * numero
            fila_resultado.append(producto)
        x.append(fila_resultado)
    return x

def producto_matrices(matriz_1, matriz_2):
    num_filas = len(matriz_1)
    num_columnas = len(matriz_2[0])
    resultado = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]
    for i in range(num_filas):
        for j in range(num_columnas):
            for a in range(len(matriz_2)):
                resultado[i][j] += matriz_1[i][a] * matriz_2[a][j]
    return resultado

def suma_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def suma_diagonal_inversa(matriz):
    suma = 0
    num_filas = len(matriz)
    for i in range(num_filas):
        suma += matriz[i][num_filas - i - 1]
    return suma

def calcular_media_matriz(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    suma_total = 0
    cantidad_elementos = num_filas * num_columnas
    for fila in matriz:
        for elemento in fila:
            suma_total += elemento
    media = suma_total / cantidad_elementos
    return media

while True:
    print("Menú:")
    print("1. Generar Matriz Aleatoria")
    print("2. Calcular Segunda Matriz")
    print("3. Sumar Filas de la Matriz")
    print("4. Sumar Columnas de la Matriz")
    print("5. Calcular Matriz Diferencia")
    print("6. Multiplicar Matriz por un Número")
    print("7. Multiplicar Dos Matrices")
    print("8. Calcular Suma de la Diagonal Principal")
    print("9. Calcular Suma de la Diagonal Inversa")
    print("10. Calcular Media de la Matriz Resultante")
    print("11. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        matriz_uno = matriz_aleatoria(5, 5, 100, 200)
        print("Matriz aleatoria generada.")

    elif opcion == "2":
        matriz_dos = segunda_matriz(matriz_uno)
        print("\nSEGUNDA MATRIZ:")
        for fila in matriz_dos:
            print(fila)

    elif opcion == "3":
        vector_suma = sumar_filas(matriz_uno)
        print("\nVECTOR DE LAS SUMAS DE LAS FILAS:", vector_suma)

    elif opcion == "4":
        suma_columnas = sumar_columnas(matriz_uno)
        print("\nVECTOR DE LAS SUMAS DE LAS COLUMNAS:", suma_columnas)

    elif opcion == "5":
        matriz_diferencia = matriz_diferencia(matriz_uno, matriz_dos)
        print("MATRIZ DIFERENCIA:")
        for fila in matriz_diferencia:
            print(fila)

    elif opcion == "6":
        numero = int(input("Ingrese un número para multiplicar la matriz: "))
        matriz_producto = producto_matriz(matriz_uno, numero)
        print("\nMATRIZ RESULTANTE DE LA MULTIPLICACIÓN:")
        for fila in matriz_producto:
            print(fila)

    elif opcion == "7":
        matriz_producto2 = producto_matrices(matriz_uno, matriz_dos)
        print("\nMATRIZ RESULTANTE DE LA MULTIPLICACIÓN DE AMBAS MATRICES:")
        for fila in matriz_producto2:
            print(fila)

    elif opcion == "8":
        suma_diagonal = suma_diagonal_principal(matriz_uno)
        print("\nSUMA DE LA DIAGONAL PRINCIPAL DE LA PRIMERA MATRIZ:", suma_diagonal)

    elif opcion == "9":
        suma_diagonal_inversa = suma_diagonal_inversa(matriz_dos)
        print("\nSUMA DE LA DIAGONAL INVERSA DE LA SEGUNDA MATRIZ:", suma_diagonal_inversa)

    elif opcion == "10":
        media_matriz_resultante = calcular_media_matriz(matriz_producto2)
        print("\nMEDIA DE LA MATRIZ RESULTANTE:", media_matriz_resultante)

    elif opcion == "11":
        break

    else:
        print("Opción no válida. Intente de nuevo.")
