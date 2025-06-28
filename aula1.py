
import time




x = -1
type(x) == int
int == int
y = 2

w = x + y

t = "o valor de w é "

print(t + str(w))

print ( type(t) )

print ( type(x) )

print (type(1.3))

print (type(True))

if x > 0:
    print("x é positivo")
    print()
    print()
elif x < -40:
    print()
else:
    print("x é negativo")

print (bool(0))

print (bool(1))

print (bool("teste bool"))
print (bool("0"))

print (bool(int("0")))

print (bool(""))

print (bool("False"))

minha_lista = [1, 2, 3, 4, 5, 6]

print(type(minha_lista))

minha_lista.append(10)

print(minha_lista)

lista_fixa = (2,4,6,8,)
print(type(lista_fixa))

minha_lista[0] = 100

print(minha_lista)

for n in minha_lista:
    print(n)

print(n)

d = {
    'a': 1, 
    'b': "exemplo", 
    'bla': False
}

print(type(d))

print(d["bla"])

d['c'] = [2,4,6,8]

print(d)

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(m[0][2])

m[0][2] = 300
print (type (m))

print(m)

print(list(range(10)))

def divisores(n:int):
    resposta = []
    inteiros = list(range(n))
    for e in inteiros:
        e1 = e + 1
        if n % e1 == 0:
            resposta.append(e1)
           
    return resposta
 

# print(divisores(20))

def print_divisores(n):
    print("Os divisores de " + str(n) + " são:\n" + str(divisores(n)))

# print_divisores(48)

# implementar função que verifica se um número é primo ou não
# exemplo:
# is_prime(47) ----> False

def outro_divisor(n):
    resposta = []
    for k in range(n):
        
        if n % (k+1) == 0:
            resposta.append(k+1)
    return resposta




# print (outro_divisor(20))
# lista_inteiros = tuple()
# print (lista_inteiros)
# print (type(e1))



def validador_de_primos (j):
    lista_prima = [1,j]
    divisores_de_jota = divisores(j)
    if lista_prima == divisores (j):
        print (str(j) + " é primo.")
    else:
        print (str(j) + " não é primo.")


# print(validador_de_primos(12))
from typing import Callable

def print_funcion_delay(f:Callable, arg:int):
    inicio = time.time()
    print ("inicio: " + str(inicio))
    f (arg)
    fim = time.time()
    print ("fim: " + str(fim))
    print("delay: " + str(fim - inicio) + " segundos")

# print_funcion_delay(validador_de_primos, 84537697)

# lista_prima = (n,1)

#     if divisores(n) = lista_prima
#     else bool(n) = "v"
#     if divisores (n) != lista_prima
#números_primos(n):
#     print (n "é primo? ----->" str(bool(n)))

# print_números_primos(7)
