import unittest
from libro import *
from autor import *

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