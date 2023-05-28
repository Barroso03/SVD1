import numpy as np

def minimos_cuadrados(A, b):
    solucion, residuo, rank, s = np.linalg.lstsq(A, b, rcond=None)
    return solucion

# Ejemplo de uso
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

A = np.zeros((filas, columnas))  # Crear una matriz de ceros con el tamaño especificado

print("Ingrese los elementos de la matriz A:")
for i in range(filas):
    for j in range(columnas):
        A[i][j] = float(input("Elemento A[{}][{}]: ".format(i, j)))

b = np.zeros(filas)  # Crear un vector de ceros con el tamaño especificado

print("Ingrese los elementos del vector b:")
for i in range(filas):
    b[i] = float(input("Elemento b[{}]: ".format(i)))

# Llamar a la función de mínimos cuadrados
x = minimos_cuadrados(A, b)

# Imprimir la solución
print("Solución:", x)

