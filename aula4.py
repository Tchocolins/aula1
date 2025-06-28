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
    def __bool__ (self):
        return False 
    def __add__(self, other):
        
        if isinstance (other, str):
            raise PoligonError("não vai rolar")
        if bool(other):
            return self.area() + other
        else: 
            return self.area() + other.area()
        
class Triangle(Poligon):
    def __init__ (self,a,b,c,ha):
        super().__init__(3)
        self.a = a
        self.b = b
        self.c = c
        self.ha = ha
        
    def area (self):
        return self.a*self.ha/2
    def perimeter (self):
        return self.a + self.b + self.c
    

        
        
        

    
      
    


class Quad(Poligon):
    def __init__(self):
        super().__init__(4)


quad = Quad()

print(quad.sides)

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

P =Paralelogram(3,4,5)
print( P.area())
print (P.perimeter())


class Rectangle(Paralelogram):
   
    def __init__ (self, b, h):
        super().__init__(b,h,h)

class Square (Rectangle):
    def __init__ (self, b):
        super().__init__(b,b)




z = Rectangle(4,6)
print (z.area())

w= Square (4)
print (w.area())
print (Square.area(w))


o:Poligon = Square(8)

print (bool (w))
print (bool("qq"))
print (bool(6))

c = o + 38
d = o+z
#e = o + "será mesmo"
print (c)
print (d)

#para a função __add__ da classe Poligon, reimplementar para permitir a soma com outros tipos (números, etc...)
#  isinstance 
print (o + True)
print("asdas")

print (True + 5)

try:
    print (o + {})
except Exception as e:
    print(type(e))
    print(dir(e))
    print(e)

# print(o + "qwerty")

print("?!!!!!!!!!!!!!!!!!")
