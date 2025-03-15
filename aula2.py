import aula1

my_list = [1, 4, 9, 16, 25]

print(my_list.index(9))

print(my_list.reverse())
print(my_list)
y = None

# imlementar uma função otimizada da lista de divisores de um inteiro
# só fazer a iteração até a raiza quadrada do número, pegando todos os divisores poss~´veis até este momento

# dica: para verificar se um número é igual ou maior que a raiz quadrada de outro, basta fazer:
# if n*n > m: etc...

#dica 2: para abandonar a recursão dentro de um for:

for i in range(20):
    print(i)
    if i > 12:
        break

# para "pular" um iteração, use a palavra reservada continue
for i in range(20):
    if i % 5 == 0:
        continue
    print(i)


n = int(input("listar divisores de: "))

divs = aula1.divisores(n)

print("divisores: " + str(divs))