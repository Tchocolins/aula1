import aula4
import json

def serialize_polygon(polygon, filename):
        
    if isinstance (polygon, aula4.Square):
        e = {
            "type": "Square",
            "b": polygon.b
            }
        with open(filename+".json", 'w', encoding='utf-8') as arquivo:
            json.dump(e, arquivo, ensure_ascii=False, indent=4)

    elif isinstance (polygon, aula4.Rectangle):
        d = {
            "type": "Rectangle",
            "b": polygon.b,
            "h": polygon.h
        }
        with open(filename+".json", 'w', encoding='utf-8') as arquivo:
            json.dump(d, arquivo, ensure_ascii=False, indent=4)


    elif isinstance (polygon, aula4.Paralelogram):
        f = {
            "type": "Paralelogram",
            "b": polygon.b,
            "a": polygon.a,
            "h": polygon.h
        }
        with open(filename+".json", 'w', encoding='utf-8') as arquivo:
            json.dump(f, arquivo, ensure_ascii=False, indent=4)

    elif isinstance (polygon, aula4.Triangle):
        g = {
            "type": "Triangle",
            "b": polygon.b,
            "a": polygon.a,
            "c": polygon.c,
            "ha": polygon.ha
        }
        with open(filename+".json", 'w', encoding='utf-8') as arquivo:
            json.dump(g, arquivo, ensure_ascii=False, indent=4)
    else:
        raise Exception ("implementa aí vagaba")
    
    # implementar a serialização para todos os polígonos já definidos
testeee = aula4.Triangle (1,2,3,4)
testee = aula4.Square (1)
teste = aula4.Paralelogram (1,2,3) 


serialize_polygon (testeee, "u")
serialize_polygon (testee, "testeII")
serialize_polygon (teste, "testeIII")