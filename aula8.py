import json

module_dict = vars()

class PoligonError(AttributeError):
    def __init__(self, msg):
        super().__init__(msg)

class Poligon():
    
    def __init__(self, sides):
        self.sides = sides
    def area(self):
        raise Exception("Você precisa implementar este método em uma subclasse")
    def perimeter(self):
        raise Exception("Você precisa implementar este método em uma subclasse")
    def toDict (self):
        d = vars(self)     
        t = type(self)
        className = None
        for key in module_dict:
            value = module_dict[key]
            if value == t:
                className = key
                break
        if not className:
            raise Exception("classe não encontrada")
        d["type"] = className
        return dict(d)
    def __bool__ (self):
        return False 
    def __add__(self, other):
        
        if isinstance (other, str):
            raise PoligonError("não vai rolar")
        if bool(other):
            return self.area() + other
        else: 
            return self.area() + other.area()
    
    def serialize (self,filename): 
        with open(filename+".json", 'w', encoding='utf-8') as arquivo:
            json.dump(self.toDict(), arquivo, ensure_ascii=False, indent=4)

    def deserialize(poligonData):
        class_name = poligonData["type"]
        clazz = module_dict[class_name]
        return clazz.buildFromDict(poligonData)
        
    

    def buildFromDict(data):
        raise Exception("Você precisa implementar este método estático na classe " + data["type"])
    
        
class Triangle(Poligon):
    def __init__ (self,a,b,c,ha):
        super().__init__(3)
        self.a = a
        self.b = b
        self.c = c
        self.ha = ha
    def toDict(self):
        return {
            "type": "Triangle",
            "b": self.b,
            "a": self.a,
            "c": self.c,
            "ha": self.ha
        }
    def buildFromDict(poligonData):
        return Triangle(poligonData["a"], poligonData["b"],  poligonData["c"], poligonData["ha"])
    def area (self):
        return self.a*self.ha/2
    def perimeter (self):
        return self.a + self.b + self.c
    

class Quad(Poligon):
    def __init__(self):
        super().__init__(4)
    
    

class Paralelogram(Quad):

    def __init__(self,b,h,a):
        super().__init__()
        self.a = a
        self.b = b
        self.h = h

    def area (self):
        return self.b * self.h
    def perimeter (self):
        return self.b *2 + self.a *2
    def buildFromDict(poligonData):
        return Paralelogram(poligonData["a"], poligonData["b"], poligonData["h"])
      


class Rectangle(Paralelogram):
   
    def __init__ (self, b, h):
        super().__init__(b,h,h)

    def buildFromDict(poligonData):
        return Rectangle(poligonData["b"], poligonData["h"])


class Square (Rectangle):
    def __init__ (self, b):
        super().__init__(b,b)
    def toDict(self):
        return {
            "type": "Square",
            "b": self.b
            }
    def buildFromDict(poligonData):
        return Square(poligonData["b"])
    
# def buildPoligon(dataFile):
    
#     with open(dataFile, 'r') as file:
#         poligonData = json.load(file)
#         if poligonData['type'] == 'Rectangle':
#             return Rectangle(poligonData['b'], poligonData['h'])

#         if poligonData['type'] == 'Square':
#             return Square(poligonData['a'])
    
#         if poligonData['type'] == 'Paralelogram':
#             return Paralelogram(poligonData['b'], poligonData['h'], poligonData ['a'])
#         if poligonData ['type'] == 'Triangle':
#             return Triangle (poligonData['a'], poligonData ['b'], poligonData ['c'], poligonData ['ha'])
#         else:
#             raise Exception("Not implemented type")


    
oo = Paralelogram(3,4,5)
oo.serialize("rect1")
Paralelogram.serialize(oo, "rect2")




### implementar a função buildFrmDict para cada classe
### criar uma classe que contem uma lista de polígonos e implementar serialização e deseriaização desta classe.



class ListaPolígonos:

    def __init__(self):
        self.polygons = []

    def addPolygon (self, poligon):
        if isinstance (poligon, Poligon):
            self.polygons.append(poligon)
        else:
            raise Exception ("poligon precisa ser um Poligon")
        
    def serialize (self,filename):
        polygonsDict = []
        for poligon in self.polygons:
            polygonsDict.append(poligon.toDict())
        with open(filename+".json", 'w', encoding='utf-8') as arquivo:
            json.dump(polygonsDict, arquivo, ensure_ascii=False, indent=4)

    def deserialize (self, filename):
        with open(filename+".json", 'r', encoding='utf-8') as arquivo:
            poligons = json.load(arquivo)
            for polígono in poligons:
                polígono_deserializado = Poligon.deserialize(polígono)
                self.addPolygon(polígono_deserializado)
    
    def deserialize2 (filename):
        lista = ListaPolígonos()
        with open(filename+".json", 'r', encoding='utf-8') as arquivo:
            poligons = json.load(arquivo)
            for polígono in poligons:
                polígono_deserializado = Poligon.deserialize(polígono)
                lista.addPolygon(polígono_deserializado)
        return lista
    
# l = ListaPolígonos();      
# l.addPolygon(Rectangle())
# ListaPolígonos.addPolygon(l, Rectangle())

    
def testAddpolygon():
    lista = ListaPolígonos()
    r = Rectangle(2,4)
    i = Square(2)
    o = Paralelogram(1,2,3)
    lista.addPolygon(r)
    lista.addPolygon(i)
    lista.addPolygon(o)
    if len(lista.polygons) != 3:
        print("Erro testAddpolygon !!!!!!!")
    else:
        print("sucesso testAddpolygon!!!!!!")

testAddpolygon()

def testSerializepolygon():
    lista = ListaPolígonos()
    r = Rectangle(2,4)
    i = Square(2)
    o = Paralelogram(1,2,3)
    lista.addPolygon(r)
    lista.addPolygon(i)
    lista.addPolygon(o)
    lista.serialize("teste")
    
# testSerializepolygon()

def testDeserializepolygons():
    lista = ListaPolígonos()
    lista.deserialize('teste')
    print (lista.polygons)

testDeserializepolygons ()


def testDeserialize2polygons():
    lista = ListaPolígonos.deserialize2('teste')
    print (lista.polygons)

testDeserialize2polygons ()