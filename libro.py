class Libro:

    def __init__(self, autor, titulo, anyo):

        self.__autor= autor
        self.__titulo = titulo
        self.__anyo = anyo


    def get_titulo(self):
        return self.__titulo

    def get_anyo(self):
        return self.__anyo