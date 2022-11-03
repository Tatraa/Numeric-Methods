import numpy as np
import matplotlib.pyplot as plt
import time

N = 50
b = [5] * N
booltemp = False

def checkFromNumpy():
    A = np.ones((N, N))
    A += np.diag([9] * N)
    A += np.diag([7] * (N - 1), 1)

    start = time.time()

    np.linalg.solve(A, b)

    end = time.time()-start

    if(not booltemp):
        print('Rozwiazanie wektoru y (Algorytm Numpy):')
        print(np.linalg.solve(A, b))
        print('Czas algorytmu:')
        print(end)
    else:
        return end

def shermanMorrison():
    matrix = []
    matrix.append([9] * N)
    matrix.append([7] * (N - 1) + [0])

    start = time.time()

    # Backward subtitution
    z = [0] * N
    x = [0] * N
    z[N - 1] = b[N - 1] / matrix[0][N - 1]
    x[N - 1] = 1 / matrix[0][N - 1]

    for i in range(N - 2, -1, -1):
        z[i] = (b[N - 2] - matrix[1][i] * z[i + 1]) / matrix[0][i]
        x[i] = (1 - matrix[1][i] * x[i + 1]) / matrix[0][i]


    mor = sum(z)/(1+sum(x))

    y=[]
    for i in range(len(z)):
        y.append(z[i] - x[i] * mor)

    end = time.time()-start

    if(not booltemp):
        print('Rozwiazanie wektoru y (Algorytm Reczny):')
        print(y)
        print('Czas algorytmu:')
        print(end)
    else:
        return end

shermanMorrison()
print()
checkFromNumpy()   

# Testing
# More gap we doing beetween in the loop on line 70 the faster it compiles, which is obvious because there is not as many dots to render, be patient :)

booltemp = True
temp = []
num = []
mine = []

for i in range(1, 2000, 3):
    N = i
    temp.append(N)
    b = [5] * N

    num.append(checkFromNumpy())
    mine.append(shermanMorrison())

# matplotlib
plt.grid(True)
plt.title('Czas pracy programu')
plt.xlabel('N - Rozmiar macierzy')
plt.ylabel('ms - Czas kompilacji')
plt.yscale('log')

plt.plot(temp, num)
plt.plot(temp, mine)
plt.legend(['Czas pracy biblioteki numpy', 'Czas pracy zaimplementowanego algorytmu'])
plt.show()