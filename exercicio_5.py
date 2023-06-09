from sympy import Symbol, solve, exp, sin

c = 1818 % 10


def primeira_equacao(x):
    return exp(-x - 1) + exp(-x - 3) + exp(x) + 5 * (c + 1)


def segunda_equacao(x):
    return (c + 2) * x ** 3 - (c + 1) * x ** 2 - 5 * x + 4 * c


def terceira_equacao(x):
    return 2 * sin(4 * (c - 3) * x) - 10


x = Symbol("x")

y = primeira_equacao(x)

print("Resultado primeira equação, x =", solve(y), "\n")

y = segunda_equacao(x)

print("Resultado segunda equação, x =",  solve(y), "\n")

y = terceira_equacao(x)

print("Resultado terceira equação, x =", solve(y), "\n")
