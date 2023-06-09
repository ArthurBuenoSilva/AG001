from sympy import Integral, Symbol

c = 1818 % 10


def my_function(x):
    return (1/5) * x**2 + (x**4)**(1/5) + (c + 3)*x - 10


x = Symbol("x")

trabalho = Integral(my_function(x), (x, 1, 12)).doit()

print("O trabalho realizado pela força entre as posições x = 1m e x = 12m é", trabalho, "J")
