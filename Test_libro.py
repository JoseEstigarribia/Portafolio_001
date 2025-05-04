import unittest
from libro import Libro #importamos la clase

class TestLibro(unittest.TestCase): #Heredamos de unittest

    def setUp(self):
        # Esta función se ejecuta antes de cada prueba.
        self.libro = Libro("Quijote", "Quiroga", 1830, "Sol y luna")

    def test_get_titulo(self):
        # Verifica que el título sea el esperado
        self.assertEqual(self.libro.get_titulo(),"Quijote")
    def test_get_autor(self):
        # Verifica que el autor sea el esperado
        self.assertEqual(self.libro.get_autor(),"Quiroga")
    def test_get_anio(self):
        #Verificar que el anio sea el indicado
        self.assertEqual(self.libro.get_anio(), 1830)
    def test_get_editorial(self):
        # Verifica que la editorial sea el esperado
        self.assertEqual(self.libro.get_editorial(),"Sol y luna")


    def test_set_titulo(self):
        self.libro.set_titulo("nuevo titulo")
        # Verifica que el título sea el esperado
        self.assertEqual(self.libro.get_titulo(),"nuevo titulo")
    def test_set_autor(self):
        self.libro.set_autor("nuevo autor")
        # Verifica que el autor sea el esperado
        self.assertEqual(self.libro.get_autor(),"nuevo autor")
    def test_set_anio(self):
        self.libro.set_anio(2331)
        #Verificar que el anio sea el indicado
        self.assertEqual(self.libro.get_anio(), 2331)
    def test_set_editorial(self):
        self.libro.set_editorial("nuevo editorial")
        # Verifica que la editorial sea el esperado
        self.assertEqual(self.libro.get_editorial(),"nuevo editorial")
 
    def test_anioinvalido_init(self):
        with self.assertRaises(ValueError):
            Libro("Quijote", "Quiroga", -0, "Sol y luna")

    def test_anioinvalido_setanio(self):
        with self.assertRaises(ValueError):
            self.libro.set_anio(0)

    def test_str(self):
        esperado = f"Titulo del Libro : {self.libro.get_titulo()} , Autor : {self.libro.get_autor()} , Año : {self.libro.get_anio()} , Editorial : {self.libro.get_editorial()}"  
        self.assertEqual(str(self.libro), esperado)



if __name__ == '__main__':
    unittest.main()
















