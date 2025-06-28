
o = [1,2,3]
o[0] = 3
print (o)

class Matrix():
    def __init__ (self,m,n):
        self.m = m
        self.n = n
        self.matrix = tuple(list(0 for y in range(n)) for x in range(m))

    def __str__(self):
        
        return "[\n" + str(self.matrix) \
            .replace("], ","\n") \
            .replace("[","") \
            .replace("])","\n]") \
            .replace("(","") \
            .replace(",", "") \
            .replace(" ", "\t\t")
    
    def linha(self, m, *args):
        # IMPLEMENTAR : USAR O MENOR LENGTH ENTRE ARGS E MATRIX[M]
        if len(self.matrix[m]) <= len(args):
            for i in range(len(self.matrix[m])):
                self.matrix[m][i] = args[i]
        else: 
            for i in range(len(args)):
                self.matrix[m][i] = args[i]

    def set_valor (self,m,n,valor):
        self.matrix[m][n] = valor
        
    def __getitem__(self, i):
        return self.matrix[i]
    
    



    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise Exception ("As matrizes precisam ter o mesmo número de linhas e de colunas para serem somadas")
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    self.matrix[i][j] =  self.matrix[i][j] + other.matrix[i][j]
        
        return "[\n" + str(self.matrix) \
            .replace("], ","\n") \
            .replace("[","") \
            .replace("])","\n]") \
            .replace("(","") \
            .replace(",", "") \
            .replace(" ", "\t\t")
    
    def mul_parcial (self,other,m,n):
        soma = 0
        for i in range(self.n):
            soma = soma + self[m][i] * other[i][n]
        return soma
    
    def mul_parcial2 (self,other,m,n):
        return sum([self.matrix[m][i] * other.matrix[i][n] for i in range(self.matrix[m])])
    
    def __mul__(self, other):
        if self.n != other.m:
            raise Exception ("erro de multiplicação: o número de colunas do primeiro deve ser igual ao número de linhas do segundo")
        
        resultante = Matrix(self.m, other.n)
        for j in range(resultante.n):
            for i in range(resultante.m):
                resultante[i][j] = self.mul_parcial(other, i, j)
        return resultante


    # TESTES   

# q = tuple(tuple(y*x for y in range(n)) for x in range(m))

# teste = Matrix(3,4)
# teste.linha(1, 3.4, -23, 56, 6)
# teste.linha(0,2,3)
# teste2 = Matrix (4,3)
# teste2.linha(1,1,2,3,)

# print(teste)
# print(teste2)
# print (teste + teste2)

# print(teste[2][1])

# teste[2][3] = 7.8

# print(teste)

# print(teste)
# print(teste2)
# print (teste * teste2)

# seja a matriz A = [[1,2,3], [2,3,4]] e a matriz B = [[1,2], [2,3], [3,4]]
matrixA = Matrix(2,3)
matrixB = Matrix(3,2)

matrixA.linha(0,1,2,3)
matrixA.linha(1,2,3,4)
matrixB.linha(0,1,2)
matrixB.linha(1,2,3)
matrixB.linha(2,3,4)
print (matrixA)
print (matrixB)
print (matrixA*matrixB)

print (matrixA.mul_parcial(matrixB,0,0))