print ([1, 5] == (1, 5))

def cube(n:int):
    return n*n*n

import aula1

aula1.print_funcion_delay(cube, 345)

class ClubeEstatistica:

    def __init__(self):
        self.nome = str(self)
        self.jogos = 0
        self.vitorias = 0
        self.derrotas = 0


    def print(self):
        print("nome: " + self.nome)
        print("jogos: " + str(self.jogos))
        print("vitórias: " + str(self.vitorias))
        print("derrotas: " + str(self.derrotas))
        print("empates: " + str(self.empates()))
        print("pontuação: " + str(self.pontuação()))
    
    def empates(self):
        return self.jogos - self.vitorias - self.derrotas
    
    def pontuação(self):
        return (self.vitorias * 3) + self.empates() 

palmeiras = ClubeEstatistica

palmeiras.print()

palmeiras.jogos += 1
palmeiras.vitorias += 1

palmeiras.print()

palmeiras.jogos += 4
palmeiras.derrotas += 1
palmeiras.vitorias += 2

palmeiras.print()

# # print(vars(palmeiras))
# # print(dir(palmeiras))

# # # implementar pontos ganhos na classe ClubeEstatistica
# # # investigar mais a fundo a função range
# # n=2
# # w= n+1
# # q = w + 3
# # for i in range (3,100,n*w*q):
# #     print (i)

# # z = "abacaxi"
# # for a in range(len(z)):
# #     print (a)


# teste_lista = [
#             ["da","oioi","asd",4]
#             ["s", "iiiii", "sera", 2]
# ]         

# for i in range(len(z)):
#     print (teste_lista [i][1])
