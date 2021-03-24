from libro import *
from autor import *

def get_list(file):
    f = open(file, mode="rt", encoding="utf-8")

    res= {len(word): [] for line in f for word in line.split(" ") if word != ""} 

    if(len(res) == 0):
        raise ValueError("Fichero vacío")

    f.seek(0)
    for line in f:
        #if line == "":        
        for word in line.split(" "):
            if not word in res[len(word)]:
                res[len(word)].append(word)
        print(line)
    
    f.close()
    return res

def mas_antiguo(lista, anyo):
    
    if anyo < 1900 or anyo > 2021:
        raise ValueError("El año no es válido")

    res= []
    for libro in lista:
        if libro.get_anyo() <= anyo:
            res.append(libro.get_titulo())

    return res

#------------main-------------
print(get_list("pruebas.txt"))

lista= [Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves1",1932),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves2",1950),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves3",1960),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves4",2020),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves5",2000)]
print(mas_antiguo(lista, 2001))