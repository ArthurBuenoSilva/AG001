from sympy import Derivative, Symbol

c = 1818 % 10


def my_function(t):
    return (t**(1/3)) / 5 + (c + 1) / (t**3) + ((c + 2) * t**2) - 15


t = Symbol("t")

velocidade = Derivative(my_function(t), t).doit()

print("A equação da velocidade:", velocidade)

velocidade_t_7 = velocidade.subs({t: 7})

print("A velocidade em t = 7s:", velocidade_t_7, "m/s")

aceleracao = Derivative(velocidade, t).doit()

print("A equação da aceleração:", aceleracao)

aceleracao_t_2 = aceleracao.subs({t: 2})

print("A aceleração em t = 2s:", aceleracao_t_2, "m/s**2")
