x = -1

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

print(m)

print(list(range(10)))

def divisores(n):
    resposta = []
    for e in range(n):
        e1 = e + 1
        if n % e1 == 0:
            resposta.append(e1)
    return resposta

print(divisores(20))

def print_divisores(n):
    print("Os divisores de " + str(n) + " são:\n" + str(divisores(n)))

print_divisores(48)

# implementar função que verifica se um número é primo ou não
# exemplo:
# is_prime(47) ----> False