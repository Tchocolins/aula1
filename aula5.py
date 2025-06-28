import math
import aula4
import json

print(dir(math))
print(math.gcd(5, 8))


print(math.log10(100))
print(math.exp(1))
print(math.log(math.exp(1)))

f = open("ex.txt", "r")
print(f.read(5))
print(f.read(5))
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("ex.txt", "a")
f.write("\nnovo conteudo\n")
f.write("novo conteudo 2\t\tetc...")
f.close()


rect = aula4.Rectangle(35, 6)


def buildPoligon(dataFile):
    # Open and read the JSON file
    with open(dataFile, 'r') as file:
        poligonData = json.load(file)
        if poligonData['type'] == 'Rectangle':
            return aula4.Rectangle(poligonData['b'], poligonData['h'])

        if poligonData['type'] == 'Square':
            return aula4.Square(poligonData['a'])
    
        if poligonData['type'] == 'Paralelogram':
            return aula4.Paralelogram(poligonData['b'], poligonData['h'], poligonData ['a'])
        if poligonData ['type'] == 'Triangle':
            return aula4.Triangle (poligonData['a'], poligonData ['b'], poligonData ['c'], poligonData ['ha'])
        else:
            raise Exception("Not implemented type")
    
r = buildPoligon("poligonR.json")
s = buildPoligon('poligonP.json')
c = buildPoligon('poligonS.json')
v = buildPoligon ('poligonT.json')

print(type(r))
print(r.b)
print(r.h)

print(type(c))
print(c.a)


print(type(s))
print(s.b)
print(s.h)
print(s.a)

print(type(v))
print(v.b)
print(v.c)
print(v.a)
print(v.ha)
# extender a função buildPoligon para todos os tipos de polígonos da aula4







