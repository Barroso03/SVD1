import numpy as np

def calcular_pseudoinversa(A):
    U, S, VT = np.linalg.svd(A)  # Descomposición en valores singulares
    S_pseudo = np.zeros(A.shape).T
    S_pseudo[:len(S), :len(S)] = np.linalg.inv(np.diag(S))  # Inversa de los valores singulares
    pseudoinversa = np.dot(VT.T, np.dot(S_pseudo, U.T))  # Cálculo de la pseudoinversa
    return pseudoinversa

# Ejemplo de uso
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

A = np.zeros((filas, columnas))  # Crear una matriz de ceros con el tamaño especificado

print("Ingrese los elementos de la matriz A:")
for i in range(filas):
    for j in range(columnas):
        A[i][j] = float(input("Elemento A[{}][{}]: ".format(i, j)))

# Calcular la pseudoinversa de A
pseudoinversa = calcular_pseudoinversa(A)

# Imprimir la pseudoinversa
print("Pseudoinversa de A:")
print(pseudoinversa)
