import numpy as np

# Función para descomponer una matriz en valores singulares
def descomponer_valores_singulares(matriz):
    # Calcula los valores singulares y los vectores singulares de la matriz
    U, s, V = np.linalg.svd(matriz)
    
    # Devuelve los resultados de la descomposición
    return U, s, V

# Ejemplo de uso
# Ingresa una matriz de ejemplo
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

matriz = np.zeros((filas, columnas))
for i in range(filas):
    for j in range(columnas):
        valor = float(input("Ingresa el valor para la posición ({}, {}): ".format(i, j)))
        matriz[i, j] = valor

# Llama a la función para descomponer la matriz en valores singulares
U, s, V = descomponer_valores_singulares(matriz)

# Imprime los resultados
print("Matriz original:")
print(matriz)
print("Matriz U:")
print(U)
print("Valores singulares:")
print(s)
print("Matriz V^t:")
print(V)
