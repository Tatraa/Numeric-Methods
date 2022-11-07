from functools import reduce
import numpy as np
import time

N = 100

# Test for checking the time for numpy library
def checkFromNumpy():
    A = np.diag([0.2] * (N - 1), -1)
    A += np.diag([1.2] * N)
    A += np.diag([0.1 / i for i in range(1, N)], 1)
    A += np.diag([0.4 / i**2 for i in range(1, N - 1)], 2)
    x = list(range(1, N + 1))
    
    start = time.time()

    np.linalg.solve(A, x)

    end = time.time()-start
    print("Czas programu napisane z pomoca biblioteki numpy to = {:.10f}".format(end))

def ownMethod():
    # Make the matrix
    matrix = []        
    matrix.append([0] + [0.2] * (N - 1))
    matrix.append([1.2] * N)
    matrix.append([0.1 / i for i in range(1, N)] + [0])
    matrix.append([0.4 / i**2 for i in range(1, N - 1)] + [0]+[0])

    # Vector x
    x = list(range(1, N + 1))

    start = time.time()

    # LU 
    for i in range(1, N-2):
        matrix[0][i] = matrix[0][i] / matrix[1][i - 1]
        matrix[1][i] = matrix[1][i] - matrix[0][i] * matrix[2][i - 1]
        matrix[2][i] = matrix[2][i] - matrix[0][i] * matrix[3][i - 1]

    matrix[0][N - 2] = matrix[0][N - 2] / matrix[1][N - 3]
    matrix[1][N - 2] = matrix[1][N - 2] - matrix[0][N - 2] * matrix[2][N - 3]
    matrix[2][N - 2] = matrix[2][N - 2] - matrix[0][N - 2] * matrix[3][N - 3]

    matrix[0][N - 1] = matrix[0][N - 1] / matrix[1][N - 2]
    matrix[1][N - 1] = matrix[1][N - 1] - matrix[0][N - 1] * matrix[2][N - 2]

    # Forward substitution
    for i in range(1, N):
        x[i] = x[i] - matrix[0][i] * x[i - 1]

    # Backward substitution
    x[N - 1] = x[N - 1] / matrix[1][N - 1]
    x[N - 2] = (x[N - 2] - matrix[2][N - 2] * x[N - 1]) / matrix[1][N - 2]

    for i in range(N - 3, -1, -1):
        x[i] = (x[i] - matrix[3][i] * x[i + 2] - matrix[2][i] * x[i + 1]) / matrix[1][i]

    # Det of matrix
    det = reduce(lambda a, b: a*b, matrix[1])

    end = time.time()-start

    print("Szukane rozwiazanie to =", x)
    print()
    print("Wyznacznik macierzy A =", det)

    print("Czas programu zaimplementowany wlasna metoda to = {:.10f}".format(end))

''' Main '''
ownMethod()
checkFromNumpy()
