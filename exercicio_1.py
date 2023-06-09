from sympy import Limit, Symbol, S

c = 1818 % 10


def my_function(x):
    return ((c + 1) - x**(1/2)) / ((c + 1)**2 - x)


x = Symbol("x")

limit_1 = Limit(my_function(x), x, (c + 1)**2).doit()

print("Limite para x -> (c + 1)**2:")
print(limit_1)

limit_2 = Limit(my_function(x), x, S.Infinity).doit()

print("Limite para x -> oo:")
print(limit_2)

limit_3 = Limit(my_function(x), x, -S.Infinity).doit()

print("Limite para x -> -oo:")
print(limit_2)
