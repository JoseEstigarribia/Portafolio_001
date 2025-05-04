"""Desarrollar la clase Libro, que tiene los siguientes atributos:

titulo: un string con el título del libro

autor: un string con el nombre del autor

anio: un entero con el año de publicación

editorial: un string con el nombre de la editorial

Y los siguientes métodos:

__init__(titulo, autor, anio, editorial)

get_titulo(), get_autor(), get_anio(), get_editorial()

set_titulo(nuevo_titulo), set_autor(nuevo_autor), set_anio(nuevo_anio), set_editorial(nueva_editorial)

__str__() → para mostrar la información completa del libro en un print()

"""

class Libro():
    def __init__(self, titulo : str, autor : str, anio : int, editorial : str):
        if anio <= 0:
            raise ValueError("Valor del año debe ser mayor que cero")
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._editorial = editorial

    def get_titulo(self):
        return self._titulo
    def get_autor(self):
        return self._autor
    def get_anio(self):
        return self._anio
    def get_editorial(self):
        return self._editorial
    
    def set_titulo(self, nuevo_titulo:str):
        self._titulo = nuevo_titulo
    def set_autor(self, nuevo_autor:str):
        self._autor = nuevo_autor
    def set_anio(self, nuevo_anio:int):
        if nuevo_anio <= 0:
            raise ValueError("Valor del año debe ser mayor acero")
        self._anio = nuevo_anio
    def set_editorial(self, nuevo_editorial:str):
        self._editorial = nuevo_editorial

    def __str__(self):
        return f"Titulo del Libro : {self.get_titulo()} , Autor : {self.get_autor()} , Año : {self.get_anio()} , Editorial : {self.get_editorial()}"  