def get_list(file):

    f = open(file, mode="rt", encoding="utf-8")
    for line in f:
        if line == "":

        print(line)
    
    f.close()




from libro import *
from autor import *

def mas_antiguo(lista, anyo):
    
    if anyo < 1900 or anyo > 2021:
        raise ValueError("El año no es válido")

    res= []
    for libro in lista:
        if libro.get_anyo() <= anyo:
            res.append(libro.get_titulo())

    return res

class Pruebas(unittest.TestCase):
    def test_value_error(self):
        lista= [Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves1",1932),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves2",1950),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves3",1960),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves4",2020),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves5",2000)]
        self.assertRaisesRegex(ValueError, "El año no es válido", mas_antiguo, lista, 1800)
        self.assertRaisesRegex(ValueError, "El año no es válido", mas_antiguo, lista, 2040)

    def test_lista_vacia(self):
        lista= []
        self.assertEqual(mas_antiguo(lista,1930), [])

    def test_resultados_esperables(self):
        lista= [Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves1",1932),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves2",1950),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves3",1960),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves4",2020),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves5",2000)]
        self.assertEqual(mas_antiguo(lista,1920), [])
        self.assertEqual(mas_antiguo(lista,1940), ["Blancanieves1"])
        self.assertEqual(mas_antiguo(lista,1955), ["Blancanieves1","Blancanieves2"])
        self.assertEqual(mas_antiguo(lista,1965), ["Blancanieves1","Blancanieves2","Blancanieves3"])
        self.assertEqual(mas_antiguo(lista,2005), ["Blancanieves1","Blancanieves2","Blancanieves3","Blancanieves5"])
        self.assertEqual(mas_antiguo(lista,2020), ["Blancanieves1","Blancanieves2","Blancanieves3","Blancanieves4","Blancanieves5"])

if __name__ == "__main__":
    unittest.main()

#------------main-------------
get_list("pruebas.txt")

lista= [Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves1",1932),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves2",1950),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves3",1960),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves4",2020),Libro(Autor(1,"Edgar", "Allan Poe"),"Blancanieves5",2000)]
print(mas_antiguo(lista, 2001))