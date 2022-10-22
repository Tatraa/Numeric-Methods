import numpy as np
import matplotlib.pyplot as plt
import sys

def der1(system, fn, x, h):
    return system((fn(x + h) - fn(x)) / h)

def der2(system, fn, x, h):
    return system((fn(x + h) - fn(x - h)) / (2 * h))

def diff(system, der, fn, x, h, df):
    return np.absolute(der(system, fn, x, h) - df)

# Function to write diagram in log scale
def diagram():
	# Grid on and visible
    plt.grid(True)
    plt.title('Blad przyblizenia pochodnej funkcji sin(x) w punkcie')
    plt.xlabel('h')
    plt.ylabel("$|D_hf - f'|$")
    # Make a plot with log scaling on both the x and y axis
    plt.loglog(h, diff(system, der1, fn, x, h, df))
    plt.loglog(h, diff(system, der2, fn, x, h, df))
    plt.legend(['Pochodna podpunkt a', 'Pochodna podpunkt b'])
    plt.savefig(name)

def ploterr():
    a = diff(system, der1, fn, x, h, df)
    b = diff(system, der2, fn, x, h, df)

    print("      Blad ze wzoru podpunktu a):")
    print('                 h | blad               ')
    print('---------------------------------------')
    for i in range(number):
        print('{0:18.{2}f} | {1:.{2}f}'.format(h[i], a[i], np.absolute(precision)))
        print('---------------------------------------')

    print("\n      Blad ze wzoru podpunktu b):")
    print('                 h | blad               ')
    print('---------------------------------------')
    for i in range(number):
        print('{0:18.{2}f} | {1:.{2}f}'.format(h[i], b[i], np.absolute(precision)))
        print('---------------------------------------')

''' Main '''

if(len(sys.argv) != 3):
    print("Niepoprawna ilosc argumentow")
    sys.exit()

# Precision choice
if(sys.argv[1] == 'float'):
    system = np.float32
    precision = -7
    name = 'wykres-float.svg'
elif(sys.argv[1] == 'double'):
    system = np.float64
    precision = -16
    name = 'wykres-double.svg'
else:
    print("Zly argument")
    sys.exit()

# Variables
x = 0.2
number = 500
h = system(np.logspace(precision, 0, number))
df = system((np.cos(x)))
fn= np.sin
# I don't know why np.sin(x) not compiling, but np.sin works

if(sys.argv[2] == 'wykres'):
    diagram()
elif(sys.argv[2] == 'blad'):
    ploterr()
else:
    print("Zly argument")
    sys.exit()