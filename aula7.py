import aula4
import json 

with open("cena.json", 'r') as file:
    poligonData = json.load(file)

print (poligonData)

### 1) Instanciar 3 polígonos
### 2) Salvar os polígonos em um json único
### 3) Abrir o arquivo json
### 4) Recriar os polígonos a partir do json aberto

polígono1 = aula4.Triangle(3,4,5,4)
polígono2= aula4.Square(7) 
polígono3 = aula4.Rectangle(8,2)

## TESTES:

def lista_parâmetro (lista):
    if type(lista) not in (list, tuple) or not all(isinstance(elemento, aula4.Poligon) for elemento in lista):
        raise Exception ("precisa ser uma list ou tuple, e cada elemento da lista precisa ser um aula4.Polígono")
    else:
        dicionários = []
        for elemento in lista:
            
            dicionários.append ()

        

##
e = [
     
    {"type": "Triangle",
     "a": polígono1.a,
     "b": polígono1.b,
     "c": polígono1.c,
     "ha": polígono1.ha
    },
     
    {"type": "Square",
      "bs": polígono2.b
    },

    {"type": "Rectangle",
     "br": polígono3.b,
     "hr": polígono3.h
    }
]

with open("polígonos.json", 'w', encoding='utf-8') as arquivo:
        json.dump(e, arquivo, ensure_ascii=False, indent=4)

with open("polígonos.json", 'r', encoding='utf-8') as arquivo:
    poligonos_salvos = json.load(arquivo)






    




