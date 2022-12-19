import numpy as np
import matplotlib.pyplot as plt

def main_function(x):
	return 1 / (1 + 25 * (x**2) )

def test_function1(x):
	return 1 / (1 + 10 * (x**2) )

def test_function2(x):
	return 1 / (1 + 5 * (x**2) )

def point_a(n):
	return [ -1 + 2*i/n for i in range(n+1) ]

def point_b(n):
	return np.cos( [ ( (2 * i + 1) / (2 * (n + 1) ) ) * np.pi for i in range(n+1) ] )

# Implementation of interpolation
def interpolation(function, point, arg, n):
	x = point(n)
	y = list(map(lambda a: function(a), x))

	new_y = []
	for a in arg:
		value = 0
		for i in range(n+1):
			temp = 1
			for k in range(n+1):
				if i != k:
					temp = temp * (a - x[k]) / (x[i] - x[k])

			value = value + y[i] * temp

		new_y.append(value)

	return new_y

# Create diagrams
def plots(arg):

    plt.title('Wielomiany interpolacyjne dla funkcji\n' 'f(x)=1/(1+25x^2) i siatki x_i = -1+2(i/(n+1))')
    plt.plot(arg, main_function(arg), label='f(x)')
    plt.plot(arg, interpolation(main_function, point_a, arg, 3), label='W_3(x)')
    plt.plot(arg, interpolation(main_function, point_a, arg, 7), label='W_7(x)')
    plt.plot(arg, interpolation(main_function, point_a, arg, 11), label='W_11(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.savefig("main_a.svg")
    plt.show()

    plt.title('Wielomiany interpolacyjne dla funkcji\n' 'f(x)=1/(1+25x^2) i siatki x_i= cos((2i+1)/(2(n+1))*Pi)')
    plt.plot(arg, main_function(arg), label='f(x)')
    plt.plot(arg, interpolation(main_function, point_b, arg, 3), label='W_3(x)')
    plt.plot(arg, interpolation(main_function, point_b, arg, 7), label='W_7(x)')
    plt.plot(arg, interpolation(main_function, point_b, arg, 11), label='W_11(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.savefig("main_b.svg")
    plt.show()

    plt.title('Wielomiany interpolacyjne dla funkcji\n' 'f(x)=1/(1+10x^2) i siatki x_i = -1+2(i/(n+1))')
    plt.plot(arg, test_function1(arg), label='f(x)')
    plt.plot(arg, interpolation(test_function1, point_a, arg, 3), label='W_3(x)')
    plt.plot(arg, interpolation(test_function1, point_a, arg, 7), label='W_7(x)')
    plt.plot(arg, interpolation(test_function1, point_a, arg, 11), label='W_11(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.savefig("test1_a.svg")
    plt.show()

    plt.title('Wielomiany interpolacyjne dla funkcji\n' 'f(x)=1/(1+10x^2) i siatki x_i= cos((2i+1)/(2(n+1))*Pi)')
    plt.plot(arg, test_function1(arg), label='f(x)')
    plt.plot(arg, interpolation(test_function1, point_b, arg, 3), label='W_3(x)')
    plt.plot(arg, interpolation(test_function1, point_b, arg, 7), label='W_7(x)')
    plt.plot(arg, interpolation(test_function1, point_b, arg, 11), label='W_11(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.savefig("test1_b.svg")
    plt.show()

    plt.title('Wielomiany interpolacyjne dla funkcji\n' 'f(x)=1/(1+5x^2) i siatki x_i = -1+2(i/(n+1))')
    plt.plot(arg, test_function2(arg), label='f(x)')
    plt.plot(arg, interpolation(test_function2, point_a, arg, 3), label='W_3(x)')
    plt.plot(arg, interpolation(test_function2, point_a, arg, 7), label='W_7(x)')
    plt.plot(arg, interpolation(test_function2, point_a, arg, 11), label='W_11(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.savefig("test2_a.svg")
    plt.show()

    plt.title('Wielomiany interpolacyjne dla funkcji\n' 'f(x)=1/(1+5x^2) i siatki x_i= cos((2i+1)/(2(n+1))*Pi)')
    plt.plot(arg, test_function2(arg), label='f(x)')
    plt.plot(arg, interpolation(test_function2, point_b, arg, 3), label='W_3(x)')
    plt.plot(arg, interpolation(test_function2, point_b, arg, 7), label='W_7(x)')
    plt.plot(arg, interpolation(test_function2, point_b, arg, 11), label='W_11(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.savefig("test2_b.svg")
    plt.show()

new_x = np.arange(-1.0, 1.01, 0.01)
plots(new_x)
