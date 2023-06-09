from sympy import Symbol, solve

c = 1818 % 10
v1 = 7 + (2 * c)
v2 = 12 + (2 * c)


# Equação resultante ao percorrer a primeira malha no sentido horário
def primeiraEquacao(i1, i2):
    return 25 * i1 - 10 * i2 - v1


# Equação resultante ao percorrer a segunda malha no sentido anti-horário
def segundaEquacao(i1, i2):
    return -20 * i1 - 30 * i2 - v2


# Equação resultante da relação das correntes, -I1 = I2 + I3
def terceiraEquacao(i1, i2, i3):
    return i1 + i2 + i3


i1 = Symbol('i1')
i2 = Symbol('i2')
i3 = Symbol('i3')

eq1 = primeiraEquacao(i1, i2)
eq2 = segundaEquacao(i1, i2)
eq3 = terceiraEquacao(i1, i2, i3)

resultado = solve((eq1, eq2, eq3))

print("Solução sistema de equação: ", resultado)
print(f"I1 = {resultado[i1]} A")
print(f"I2 = {resultado[i2]} A")
print(f"I3 = {resultado[i3]} A")
