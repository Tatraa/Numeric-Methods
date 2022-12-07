import numpy as np
import functools
from matplotlib import pyplot as plt
import sys

name = 'wykres.svg'

def main_a(n):
    hessenberg_matrix = [[3, 6, 6, 9],
                         [1, 4, 0, 9],
                         [0, 0.2, 6, 12],
                         [0, 0, 0.1, 6]]
    precision = (10)**(-15)

    result_QR = []

    def hessenbergQR():
        result_matrix = []
        Q,R = np.linalg.qr(hessenberg_matrix)
        for i in range(n):
            new_matrix = np.dot(R,Q)
            Q_it,R_it = np.linalg.qr(new_matrix)
            R = R_it
            Q = Q_it
            result_matrix = new_matrix
        return result_matrix


    result_matrix = hessenbergQR()
    def checkingUnderDiag(result_matrix):
        for i in range(len(result_matrix)):
            for j in range(i):
                if result_matrix[i][j] < precision:
                    result_matrix[i][j] = 0
        return result_matrix


    def w_wlasne(matrix):
        for i in range(len(matrix)):
            for j in range(i+1):
                if j == i:
                    result_QR.append(matrix[i][j])
                else:
                    pass


    result_matrix = hessenbergQR()
    result_matrix_checked = checkingUnderDiag(result_matrix)

    print("\nMacierz po przyblizonym rozkladzie QR: \n")
    print(result_matrix_checked)

    w_wlasne(result_matrix_checked)

    print("\nWartosci Wlasne Macierzy Hessenberga: \n")
    print(result_QR)
    print()

def main_b(n):
    result_vectors = []
    iterations = []
    result_values = []


    A = np.array([[3, 4, 2, 4],
                  [4, 7, 1, -3],
                  [2, 1, 3, 2],
                  [4, -3, 2, 2]])

    u = np.array([[1], [1], [1], [1]])

    eigenvalue = 0
    for i in range(n):
        u = A @ u
        eigenvalue = abs(np.linalg.norm(np.max(u)))
        u = u / eigenvalue
        iterations.append(i)
        result_values.append(eigenvalue)
        result_vectors.append(u)

    result_vectors = np.reshape(result_vectors,(n,4))

    print('Najwieksza wartosc wlasna:\n\n', eigenvalue)
    print()
    print('Wektor wlasny:\n\n', u)

    # plt.yscale("log")
    plt.grid()
    plt.title("Maksymalna wartosc wlasna wzgledem liczby iteracji")
    plt.ylabel("Najwieksza wartosc własna")
    plt.xlabel("Liczba Iteracji")
    plt.plot(iterations,result_values)
    plt.savefig(name)
    plt.show()

    print(np.linalg.eigvals(A))


''' MAIN '''
if(len(sys.argv) < 2):
	print("Za malo argumentow!")
	sys.exit()

if(len(sys.argv) > 2):
	print("Za duzo argumentow!")
	sys.exit()

if(sys.argv[1] == 'program_a'):
    main_a(100)
elif(sys.argv[1] == 'program_b'):
    main_b(100)
