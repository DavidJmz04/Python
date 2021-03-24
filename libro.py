class Libro:

    def __init__(self, autor, titulo, anyo):

        self.__autor= autor
        self.__titulo = titulo
        self.__anyo = anyo


    def get_titulo(self):
        return self.__titulo

    def get_anyo(self):
        return self.__anyo

    def mas_antiguo(self, lista, anyo):

        res= []
        for libro in lista:
            if libro.get_anyo() < 1900 or libro.get_anyo() > 2020:
                raise ValueError("El año no es válido")

            if libro.get_anyo() <= anyo:
                res.append(libro.get_titulo())
            
